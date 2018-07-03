from docutils import utils, nodes
from sphinx.util.nodes import split_explicit_title
import re

lang_prefixed_web_url_re_obj = re.compile('([a-z]+-)*(https?://[^/].*)',
                                          re.IGNORECASE)
# See https://www.w3schools.com/Tags/ref_language_codes.asp

# -----------------------------------------------------------------------------

def linklang_role(name, rawtext, text, lineno, inliner,
                  options={}, content=[]):

    unescaped_text = utils.unescape(text)
    has_explicit_title, rawtitle, lang_prefix_url \
            = split_explicit_title(unescaped_text)

    m = lang_prefixed_web_url_re_obj.match(lang_prefix_url)
    assert m, ('%s is not a valid URL for "linklang" role, http or https ' \
            + 'URL with optional language code + hyphen prefix expected ' \
            + '(e.g. fr-http://www.frenchwebsite.fr)') % lang_prefix_url

    url = m.group(2)
    if m.group(1):
        lang = m.group(1)[:-1]
        if has_explicit_title:
            title = rawtitle
        else:
            title = rawtitle[len(lang) + 1:]
    else:
        lang = ''
        title = rawtitle

    node = linklang_ref(rawtext, title, refuri=url, lang=lang, **options)
    return [node], []

# -----------------------------------------------------------------------------

class linklang_ref(nodes.reference):

    pass

# -----------------------------------------------------------------------------

def visit_linklang_ref_node_html(self, node):

    atts = {'class': 'reference external', 'href': node['refuri']}

    if node['lang']:
        atts['hreflang'] = node['lang']

    self.body.append(self.starttag(node, 'a', '', **atts))

# -----------------------------------------------------------------------------

def visit_linklang_ref_node_non_html(self, node):

    self.visit_reference(node)

# -----------------------------------------------------------------------------

def depart_linklang_ref_node(self, node):

    self.depart_reference(node)

# -----------------------------------------------------------------------------

def setup(app):

    app.add_node(linklang_ref, html=(visit_linklang_ref_node_html,
                                     depart_linklang_ref_node),
                               latex=(visit_linklang_ref_node_non_html,
                                      depart_linklang_ref_node),
                               texinfo=(visit_linklang_ref_node_non_html,
                                        depart_linklang_ref_node),
                               text=(visit_linklang_ref_node_non_html,
                                     depart_linklang_ref_node),
                               man=(visit_linklang_ref_node_non_html,
                                    depart_linklang_ref_node))
    app.add_role('linklang', linklang_role)
