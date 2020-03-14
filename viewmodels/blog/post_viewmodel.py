from badgettinggbetter.services import project_services
from badgettinggbetter.viewmodels.shared.viewmodel_base import ViewModelBase
from badgettinggbetter.data.projects import Project
# pylint: disable=no-member

class PostViewModel(ViewModelBase):
    def __init__(self, post_link_id: str):
        super().__init__()
        self.post_link_id = post_link_id