from sphinx.environment.adapters import toctree

def _get_local_toctree(builder, docname, collapse=True, **kwds):
    """Generate a local TOC tree for the given document."""
    if 'includehidden' not in kwds:
        kwds['includehidden'] = False
    
    toc_adapter = toctree.TocTree(builder.env)
    result = toc_adapter.get_toctree_for(
        docname, builder, collapse, **kwds
    )
    return result

def html_page_context(app, pagename, templatename, context, doctree):
    """Add custom toctree function to template context."""
    try:
        context['get_toctree'] = lambda **kw: _get_local_toctree(app.builder, pagename, **kw)
    except Exception as e:
        app.warn(f"Failed to add toctree to context: {e}")

def setup(app):
    """Setup the extension."""
    app.connect('html-page-context', html_page_context)
    
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
