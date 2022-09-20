'''Tests checking that parsing works'''
import pytest

@pytest.mark.parametrize('calendar_name', [
    # Issue #178 - A component with an unknown/invalid name is represented
    # as one of the known components, the information about the original
    # component name is lost.
    # https://github.com/collective/icalendar/issues/178 https://github.com/collective/icalendar/pull/180
    # Parsing of a nonstandard component
    'issue_178_component_with_invalid_name_represented',
    # Nonstandard component inside other components, also has properties
    'issue_178_custom_component_inside_other',
    # Nonstandard component is able to contain other components
    'issue_178_custom_component_contains_other'])
def test_calendar_to_ical_is_inverse_of_from_ical(calendars, calendar_name):
    calendar = getattr(calendars, calendar_name)
    assert calendar.to_ical() == calendar.raw_ics

def test_description_parsed_properly_issue_53(events):
    '''Issue #53 - Parsing failure on some descriptions?

    https://github.com/collective/icalendar/issues/53
    '''
    assert b'July 12 at 6:30 PM' in events.issue_53_description_parsed_properly['DESCRIPTION'].to_ical()

def test_tzid_parsed_properly_issue_53(timezones):
    '''Issue #53 - Parsing failure on some descriptions?

    https://github.com/collective/icalendar/issues/53
    '''
    assert timezones.issue_53_tzid_parsed_properly['tzid'].to_ical() == b'America/New_York'
