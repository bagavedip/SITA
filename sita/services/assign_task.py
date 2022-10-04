from sita.models.assign_task import AssignTask


class AssignTaskService:
    """
     Services for AssignTask models
    """

    @staticmethod
    def update(name, **kwargs):
        """
        Function update an asset from kwargs
        """
        for key, value in kwargs.items():
            setattr(name, key, value)
        name.save()

        return name

    @staticmethod
    def assign_user(selectedIncidents, userName):
        incident_list = []
        for incident in selectedIncidents:
            incident_list.append(
                AssignTask(
                    selectedIncidents=incident,
                    userName=userName
                )
            )
        user = AssignTask.objects.bulk_create(incident_list)
        return user
