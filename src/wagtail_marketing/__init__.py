default_app_config = 'wagtail_marketing.apps.WagtailMarketingConfig'

VERSION = (0, 0, 1, 'dev1')


def get_version():
    """Return normalised version string."""
    version = '%s.%s' % (VERSION[0], VERSION[1])
    # Append 3rd digit if > 0
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])

    if VERSION[3] != 'final':
        version = '%s.%s' % (version, VERSION[3])
    return version