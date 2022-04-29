from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import QuestsViewSet, StandingsViewSet, User_Quest_JoinViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("quests", QuestsViewSet)
router.register("standings", StandingsViewSet)
router.register("user_quest_join", User_Quest_JoinViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
