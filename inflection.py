"""
    inflection
    ~~~~~~~~~~~~

    A port of Ruby on Rails' inflector to Python.

    :copyright: (c) 2012 by Janne Vanhala
    :license: MIT, see LICENSE for more details.
"""
import re

__version__ = '0.1.0'

_plurals = []
_singulars = []
_uncountables = set()


def plural(rule, replacement, flags=re.IGNORECASE):
    if rule in _uncountables:
        _uncountables.remove(rule)
    if replacement in _uncountables:
        _uncountables.remove(replacement)
    _plurals.insert(0, (re.compile(rule, flags), replacement))


def singular(rule, replacement, flags=re.IGNORECASE):
    """
    Specifies a new singularization rule and its replacement. The rule can
    either be a string or a regular expression. The replacement should always
    be a string that may include references to the matched data from the rule.
    """
    if rule in _uncountables:
        _uncountables.remove(rule)
    if replacement in _uncountables:
        _uncountables.remove(replacement)
    _singulars.insert(0, (re.compile(rule, flags), replacement))


def irregular(s, p):
    """
    Specifies a new irregular that applies to both pluralization and
    singularization at the same time. This can only be used for strings, not
    regular expressions. You simply pass the irregular in singular and plural
    form.

    Examples::

        >>> irregular('octopus', 'octopi')
        >>> irregular('person', 'people')

    :param s: irregular in singular form
    :param p: irregular in plural form
    """
    if s in _uncountables:
        _uncountables.remove(s)
    if p in _uncountables:
        _uncountables.remove(p)
    if s[0].upper() == p[0].upper():
        plural(r"({0}){1}$".format(s[0], s[1:]), r'\1' + p[1:])
        plural(r"({0}){1}$".format(p[0], p[1:]), r'\1' + p[1:])
        singular(r"({0}){1}$".format(p[0], p[1:]), r'\1' + s[1:])
    else:
        plural(r"{0}(?i){1}$".format(s[0].upper(), s[1:]),
            p[0].upper() + p[1:], flags=0)
        plural(r"{0}(?i){1}$".format(s[0].lower(), s[1:]),
            p[0].lower() + p[1:], flags=0)
        plural(r"{0}(?i){1}$".format(p[0].upper(), p[1:]),
            p[0].upper() + p[1:], flags=0)
        plural(r"{0}(?i){1}$".format(p[0].lower(), p[1:]),
            p[0].lower() + p[1:], flags=0)
        singular(r"{0}(?i){1}$".format(p[0].upper(), p[1:]),
            s[0].upper() + s[1:], flags=0)
        singular(r"{0}(?i){1}$".format(p[0].lower(), p[1:]),
            s[0].lower() + s[1:], flags=0)


def uncountable(*words):
    """
    Add uncountable words that shouldn't be attempted inflected.

    Examples::

        >>> uncountable("money")
        >>> uncountable("money", "information")
    """
    for word in words:
        _uncountables.add(word)


def camelize(string, uppercase_first_letter=True):
    """
    Convert strings to CamelCase.

    Examples::

        >>> camelize("device_type")
        "DeviceType"
        >>> camelize("device_type", False)
        "deviceType"

    :func:`camelize` can be though as a inverse of :func:`underscore`, although
    there are some cases where that does not hold::

        >>> camelize(underscore("IOError"))
        "IoError"

    :param uppercase_first_letter: if set to `True` :func:`camelize` converts
        strings to UpperCamelCase. If set to `False` :func:`camelize` produces
        lowerCamelCase. Defaults to `True`.
    """
    if uppercase_first_letter:
        return re.sub(r"(?:^|_)(.)", lambda m: m.group(1).upper(), string)
    else:
        return string[0].lower() + camelize(string)[1:]


def classify():
    pass


def dasherize(word):
    """Replace underscores with dashes in the string.

    Example::

        >>> dasherize("puni_puni")
        "puni-puni"
    """
    return word.replace('_', '-')


def foreign_key():
    pass


def humanize():
    pass


def ordinalize():
    pass


def parameterize():
    pass


def pluralize(word):
    """
    Return the plural form of a word.

    Examples::

        >>> pluralize("post")
        "posts"
        >>> pluralize("octopus")
        "octopi"
        >>> pluralize("sheep")
        "sheep"
        >>> pluralize("CamelOctopus")
        "CamelOctopi"

    """
    if not word or word.lower() in _uncountables:
        return word
    else:
        for rule, replacement in _plurals:
            if rule.search(word):
                return rule.sub(replacement, word)
        return word


def singularize(word):
    """
    Return the singular form of a word, the reverse of :func:`pluralize`.

    Examples::

        >>> singularize("posts")
        "post"
        >>> singularize("octopi")
        "octopus"
        >>> singularize("sheep")
        "sheep"
        >>> singularize("word")
        "word"
        >>> singularize("CamelOctopi")
        "CamelOctopus"
    """
    for inflection in _uncountables:
        if re.search(r'\b({0})\Z'.format(inflection), word, flags=re.IGNORECASE):
            return word

    for rule, replacement in _singulars:
        if rule.search(word):
            return rule.sub(replacement, word)
    return word


def tableize():
    pass


def titleize():
    pass


def transliterate():
    pass


def underscore(word):
    word = re.sub(r"([A-Z]+)([A-Z][a-z])", r'\1_\2', word)
    word = re.sub(r"([a-z\d])([A-Z])", r'\1_\2', word)
    word = word.replace("-", "_")
    return word.lower()


plural(r"$", 's')
plural(r"s$", 's')
plural(r"^(ax|test)is$", r'\1es')
plural(r"(octop|vir)us$", r'\1i')
plural(r"(octop|vir)i$", r'\1i')
plural(r"(alias|status)$", r'\1es')
plural(r"(bu)s$", r'\1ses')
plural(r"(buffal|tomat)o$", r'\1oes')
plural(r"([ti])um$", r'\1a')
plural(r"([ti])a$", r'\1a')
plural(r"sis$", 'ses')
plural(r"([^f])fe$", r'\1ves')
plural(r"([lr])f$", r'\1ves')
plural(r"(hive)$", r'\1s')
plural(r"([^aeiouy]|qu)y$", r'\1ies')
plural(r"(x|ch|ss|sh)$", r'\1es')
plural(r"(matr|vert|ind)(?:ix|ex)$", r'\1ices')
plural(r"(m|l)ouse$", r'\1ice')
plural(r"(m|l)ice$", r'\1ice')
plural(r"^(ox)$", r'\1en')
plural(r"^(oxen)$", r'\1')
plural(r"(quiz)$", r'\1zes')

singular(r"s$", '')
singular(r"(ss)$", r'\1')
singular(r"(n)ews$", r'\1ews')
singular(r"([ti])a$", r'\1um')
singular(r"((a)naly|(b)a|(d)iagno|(p)arenthe|(p)rogno|(s)ynop|(t)he)(sis|ses)$", r'\1\2sis')
singular(r"(^analy)(sis|ses)$", r'\1sis')
singular(r"([^f])ves$", r'\1fe')
singular(r"(hive)s$", r'\1')
singular(r"(tive)s$", r'\1')
singular(r"([lr])ves$", r'\1f')
singular(r"([^aeiouy]|qu)ies$", r'\1y')
singular(r"(s)eries$", r'\1eries')
singular(r"(m)ovies$", r'\1ovie')
singular(r"(x|ch|ss|sh)es$", r'\1')
singular(r"(m|l)ice$", r'\1ouse')
singular(r"(bus)(es)?$", r'\1')
singular(r"(o)es$", r'\1')
singular(r"(shoe)s$", r'\1')
singular(r"(cris|test)(is|es)$", r'\1is')
singular(r"^(a)x[ie]s$", r'\1xis')
singular(r"(octop|vir)(us|i)$", r'\1us')
singular(r"(alias|status)(es)?$", r'\1')
singular(r"^(ox)en", r'\1')
singular(r"(vert|ind)ices$", r'\1ex')
singular(r"(matr)ices$", r'\1ix')
singular(r"(quiz)zes$", r'\1')
singular(r"(database)s$", r'\1')

irregular('person', 'people')
irregular('man', 'men')
irregular('child', 'children')
irregular('sex', 'sexes')
irregular('move', 'moves')
irregular('cow', 'kine')
irregular('zombie', 'zombies')

uncountable(
    'equipment',
    'fish',
    'information',
    'jeans',
    'money',
    'rice',
    'series',
    'sheep',
    'species',
)
