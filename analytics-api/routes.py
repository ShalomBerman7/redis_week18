from fastapi import APIRouter
import dal

router = APIRouter()


@router.get('/analytics/alerts-by-border-and-priority')
def alerts_by_border_and_priority():
    return dal.alerts_by_border_and_priority()


@router.get('/analytics/top-urgent-zones')
def top_urgent_zones():
    return dal.top_urgent_zones()


@router.get('/analytics/distance-distribution')
def distance_distribution():
    return dal.distance_distribution()


@router.get('/analytics/low-visibility-high-activity')
def low_visibility_high_activity():
    return dal.low_visibility_high_activity()


@router.get('/analytics/hot-zones')
def hot_zones():
    return dal.hot_zones()
