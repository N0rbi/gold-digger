from gameObject.gameObject import GameObject


class DynamicGameObject(GameObject):
    def __init__(self, x, y, m):
        self._vx = 0
        self._vy = 0
        super().__init__(x, y)
        self.gravity = 200.
        self.m = m

        self.forces_x = []
        self.forces_y = [self.gravity*self.m]

    def _updatePosition(self, dt):
        ax = sum(self.forces_x)/self.m
        ay = sum(self.forces_y)/self.m

        self._vx += ax * dt
        self._vy += ay * dt

        self.x += self._vx * dt
        self.y += self._vy * dt

        self.reset_forces()

    def reset_forces(self):
        self.forces_x = []
        self.forces_y = [self.gravity*self.m]

    def tick(self, dt):
        self._updatePosition(dt)
