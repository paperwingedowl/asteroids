from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle_mod = random.uniform(20,70)
        vec1 = self.velocity.rotate(angle_mod)
        vec2 = self.velocity.rotate(-angle_mod)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast_1.velocity = vec1 * 1.2
        new_ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast_2.velocity = vec2 * 1.2
    
    def update(self, delta):
        self.position += self.velocity * delta
    