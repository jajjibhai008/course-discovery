"""
Toggles for course metadata app.
"""

from edx_toggles.toggles import WaffleSwitch

# .. toggle_name: course_metadata.bypass_lms_data_loader__end_date_updated_check
# .. toggle_implementation: WaffleSwitch
# .. toggle_default: False
# .. toggle_description: Enable to bypass end date updated checks in LMS Data loader and make sure that
#     upgrade deadline information is updated in Discovery and then pushed to ecommerce if applicable.
# .. toggle_use_cases: open_edx
# .. toggle_creation_date: 2022-01-20
# .. toggle_target_removal_date: None
# .. toggle_tickets: PROD-3121
# .. toggle_warning: This flag should only be turned on if either calls to ecommerce failed or end dates were updated
#     via admin, leaving the upgrade deadline information inconsistent across Discovery and ecommerce.  Once LMS
#     data loader runs and dates are in sync, turn off this flag.
BYPASS_LMS_DATA_LOADER__END_DATE_UPDATED_CHECK = WaffleSwitch(
    'course_metadata.bypass_lms_data_loader__end_date_updated_check', __name__
)
