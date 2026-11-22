Inflection
==========

Inflection is a string transformation library.  It singularizes and pluralizes
English words, and transforms strings from CamelCase to underscored_string.
Inflection is a port of `Ruby on Rails`_' `inflector`_ to Python.

.. _Ruby on Rails: http://rubyonrails.org
.. _inflector: http://api.rubyonrails.org/classes/ActiveSupport/Inflector.html


Installation
------------

Use pip to install from PyPI::

    pip install inflection


Preserving Application-Specific Words
-------------------------------------

Inflection applies word-ending rules; it does not determine whether a word is
a noun or an adjective. To preserve known words such as ``ambitious`` and
``dangerous``, add their lowercase forms to ``inflection.UNCOUNTABLES``. This
public set is checked by both ``singularize`` and ``pluralize``, so there is no
need to call the private ``_irregular`` helper:

.. code-block:: python

    import inflection

    inflection.UNCOUNTABLES.update({'ambitious', 'obvious', 'dangerous'})
    assert inflection.singularize('ambitious') == 'ambitious'
    assert inflection.singularize('Dangerous') == 'Dangerous'
    assert inflection.pluralize('OBVIOUS') == 'OBVIOUS'
    assert inflection.singularize('houses') == 'house'

Entries match the whole input, case-insensitively, and preserve the original
capitalization. They are not suffix rules: adding ``dangerous`` does not also
preserve ``very_dangerous``. Add that complete input separately if needed.

This customization affects all callers using the module in the current Python
process. Configure it once during application initialization. If only one call
should use an exception list, keep a local set and bypass ``singularize`` for
those inputs instead:

.. code-block:: python

    preserved_words = {'ambitious', 'obvious', 'dangerous'}

    def singularize_name(word):
        if word.lower() in preserved_words:
            return word
        return inflection.singularize(word)

    assert singularize_name('Dangerous') == 'Dangerous'
    assert singularize_name('products') == 'product'


Contributing
------------

To contribute to Inflector `create a fork`_ on GitHub. Clone your fork, make
some changes, and submit a pull request.

.. _create a fork: https://github.com/jpvanhal/inflection/fork_select


API Documentation
-----------------

.. module:: inflection

.. autofunction:: camelize
.. autofunction:: dasherize
.. autofunction:: humanize
.. autofunction:: ordinal
.. autofunction:: ordinalize
.. autofunction:: parameterize
.. autofunction:: pluralize
.. autofunction:: singularize
.. autofunction:: tableize
.. autofunction:: titleize
.. autofunction:: transliterate
.. autofunction:: underscore


Changelog
---------

You you can see the full list of changes between each Inflection release in
`GitHub releases page`_.

.. _GitHub releases page: https://github.com/jpvanhal/inflection/releases


License
-------

.. include:: ../LICENSE
