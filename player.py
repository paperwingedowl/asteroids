import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.rotation = 0
        self.shot_timer = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, delta):
        self.rotation += PLAYER_TURN_SPEED * delta

    def update(self, delta):

        self.shot_timer -= delta

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-delta)
        if keys[pygame.K_d]:
            self.rotate(delta)
        if keys[pygame.K_w]:
            self.move(delta)
        if keys[pygame.K_s]:
            self.move(-delta)
        if keys[pygame.K_SPACE]:
            try:
                self.shoot()
            except Exception as e:
                pass

        if abs(self.velocity.x) > PLAYER_MAX_SPEED:
            if self.velocity.x < 0:
                self.velocity.x = -PLAYER_MAX_SPEED
            elif self.velocity.x >= 0:
                self.velocity.x = PLAYER_MAX_SPEED
        if abs(self.velocity.y) > PLAYER_MAX_SPEED:
            if self.velocity.y < 0:
                self.velocity.y = -PLAYER_MAX_SPEED
            elif self.velocity.y >= 0:
                self.velocity.y = PLAYER_MAX_SPEED
            
        self.position += self.velocity * delta
    
    def move(self, delta):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += forward * PLAYER_ACCELERATION * delta
        print(self.velocity)

    def strafe(self, delta):
        pass

    def shoot(self):
        if self.shot_timer > 0:
            raise Exception("Gun is still on cooldown...")
        self.shot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.velocity += pygame.Vector2(0, 1).rotate(self.rotation) * -25
