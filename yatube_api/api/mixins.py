from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet


class ListCreateModelViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    """A ViewSet that provides list and create actions."""

    pass
