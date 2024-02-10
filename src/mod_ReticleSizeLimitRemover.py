from AvatarInputHandler import gun_marker_ctrl


def overrideIn(cls, condition=lambda: True):

    def _overrideMethod(func):
        if not condition():
            return func

        funcName = func.__name__

        if funcName.startswith("__"):
            funcName = "_" + cls.__name__ + funcName

        old = getattr(cls, funcName)

        def wrapper(*args, **kwargs):
            return func(old, *args, **kwargs)

        setattr(cls, funcName, wrapper)
        return wrapper
    return _overrideMethod


@overrideIn(gun_marker_ctrl)
def _setupGunMarkerSizeLimits(func, dataProvider, scale=None):
    limits = func(dataProvider, scale)

    newLimits = (1.0, limits[1])
    dataProvider.sizeConstraint = newLimits

    return newLimits
