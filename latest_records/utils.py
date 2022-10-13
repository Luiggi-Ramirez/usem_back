from django.contrib.contenttypes.models import ContentType 
from django.contrib.admin.models import LogEntry, ADDITION


def custom_log_entries(user_id, model_name, object_id, obj_repr):
    '''function to add log entries via views'''

    LogEntry.objects.log_action(
        user_id=user_id,
        content_type_id=ContentType.objects.get_for_model(model_name).pk,
        object_id=object_id,
        object_repr=str(obj_repr),
        action_flag=ADDITION,
    )