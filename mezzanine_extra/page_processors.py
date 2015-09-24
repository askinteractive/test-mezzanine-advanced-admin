from mezzanine.pages.page_processors import processor_for


@processor_for('evenements')
def events_processor(request, page):
    events = page.children.published().order_by('_order')
    return {"events": events}