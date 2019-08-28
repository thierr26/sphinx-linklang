# LinkLang (Sphinx extension)

## General information

[Sphinx](http://www.sphinx-doc.org/en/master) is a documentation generator
(that can also be used as a static website generator) written in Python. Sphinx
takes as input text files in [reStructuredText format](
https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) and
can produce output in various formats, in particular in HTML.

Sphinx has [support for extensions](
http://www.sphinx-doc.org/en/master/usage/extensions). LinkLang is a Sphinx
extension that makes it possible to indicate the language of an external link
destination in the reStructuredText source and renders this information in the
HTML output. To put it another way, LinkLang makes it possible to get [hreflang
attributes](https://www.w3schools.com/Tags/att_a_hreflang.asp) in the
hyperlinks (the `<a>` tags) of Sphinx HTML output.


## Installing LinkLang in your Sphinx project

### Manually

1. Create a subdirectory called `extensions` in your Sphinx project. This new
   subdirectory should be at the same level as the `source` subdirectory.
2. Get a copy of the LinkLang source tree (that is a `sphinx-linklang`
   directory containing a `src` subdirectory, and the `src` subdirectory should
   contain the `linklang.py` file).
3. Place the whole LinkLang source tree in the `extensions` subdirectory of the
   Sphinx project.
4. Make sure you have lines like the following at the beginning of the
   `conf.py` file of your Sphinx project:
   ```python
   import os
   import sys
   sys.path.insert(0, os.path.abspath('../extensions/sphinx-linklang/src'))
   ```
5. Add LinkLang to the extensions list in the `conf.py` file of your Sphinx
   project:
   ```python
   extensions = [
       'linklang',
   ]
   ```


### As a Git submodule

If your Sphinx project is under Git version control, I suggest you install
LinkLang as a Git submodule.

Do as instructed above, but instead of the 2nd and 3rd steps, just do:
```bash
git submodule add https://github.com/thierr26/sphinx-linklang.git \
    extensions/sphinx-linklang
git submodule init # Not needed with recent versions of Git.
```


## Usage

Use the `linklang` role in your reStructuredText sources to specify the
hyperlinks that need a `hreflang` attribute:
```
:linklang:`en-http://foo.bar.com`
```
or
```
:linklang:`foo bar <en-http://foo.bar.com>`
```

`en-` prepended to the URL causes a `hreflang="en"` attribute to be added in
the `<a>` tag in the HTML output. (`en` is the language code for English. The
whole language code list is available here:
https://www.w3schools.com/Tags/ref_language_codes.asp).

Omitting the language code results in a `<a>` tag without `hreflang` attribute.


## Author

[Thierry Rascle](thierr26@free.fr)


## License

This project is licensed under the MIT License. See the LICENSE file for
details.
