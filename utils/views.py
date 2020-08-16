from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle


class OncePerDayUserThrottle(UserRateThrottle):
    rate = '24/day'


@api_view(['GET'])
@throttle_classes([OncePerDayUserThrottle])
def api_health(request):
    return Response({"message": "API running and Up!"})
