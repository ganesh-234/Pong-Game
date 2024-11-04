import sys
import pygame


class Paddle:
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed


class Ball:
    def __init__(self, x, y, size, speed):
        self.rect = pygame.Rect(x, y, size, size)  
        self.speed = speed
        self.dx = speed
        self.dy = speed

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def bounce_horizontal(self):
        self.dx = -self.dx

    def bounce_vertical(self):
        self.dy = -self.dy


class PongGame:
    def __init__(
        self,
        screen_width,
        screen_height,
        paddle_width,
        paddle_height,
        paddle_speed,
        ball_size,
        ball_speed,
        winning_score,
        frame_rate,
    ):
        pygame.init()

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle_speed = paddle_speed
        self.ball_size = ball_size
        self.ball_speed = ball_speed
        self.winning_score = winning_score
        self.frame_rate = frame_rate

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        self.player1_score = 0
        self.player2_score = 0
        self.paused = False

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Pong")

        self.font = pygame.font.Font(None, 36)

        self.player1 = Paddle(
            10,
            screen_height // 2 - paddle_height // 2,
            paddle_width,
            paddle_height,
            paddle_speed,
        )
        self.player2 = Paddle(
            screen_width - 30,
            screen_height // 2 - paddle_height // 2,
            paddle_width,
            paddle_height,
            paddle_speed,
        )
        self.ball = Ball(
            screen_width // 2 - ball_size // 2,
            screen_height // 2 - ball_size // 2,
            ball_size,
            ball_speed,
        )

        self.clock = pygame.time.Clock()

    def display_text(self, text, x, y):
        text_surface = self.font.render(text, True, self.WHITE)
        self.screen.blit(text_surface, (x, y))

    def reset_ball(self):
        self.ball.rect.x = self.screen_width // 2 - self.ball_size // 2
        self.ball.rect.y = self.screen_height // 2 - self.ball_size // 2
        self.ball.dx = self.ball_speed
        self.ball.dy = self.ball_speed

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.paused = not self.paused

            if not self.paused:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w] and self.player1.rect.top > 0:
                    self.player1.move_up()
                if keys[pygame.K_s] and self.player1.rect.bottom < self.screen_height:
                    self.player1.move_down()
                if keys[pygame.K_UP] and self.player2.rect.top > 0:
                    self.player2.move_up()
                if (
                    keys[pygame.K_DOWN]
                    and self.player2.rect.bottom < self.screen_height
                ):
                    self.player2.move_down()

                self.ball.move()

                if self.ball.rect.colliderect(
                    self.player1.rect
                ) or self.ball.rect.colliderect(self.player2.rect):
                    self.ball.bounce_horizontal()
                if (
                    self.ball.rect.top <= 0
                    or self.ball.rect.bottom >= self.screen_height
                ):
                    self.ball.bounce_vertical()

                if self.ball.rect.left < 0:
                    self.player2_score += 1
                    self.reset_ball()
                elif self.ball.rect.right > self.screen_width:
                    self.player1_score += 1
                    self.reset_ball()

                game_over = False
                if self.player1_score >= self.winning_score:
                    winner = "Player 1"
                    game_over = True
                elif self.player2_score >= self.winning_score:
                    winner = "Player 2"
                    game_over = True

            self.screen.fill(self.BLACK)

            pygame.draw.rect(self.screen, self.WHITE, self.player1.rect)
            pygame.draw.rect(self.screen, self.WHITE, self.player2.rect)
            pygame.draw.ellipse(self.screen, self.WHITE, self.ball.rect)
            pygame.draw.aaline(
                self.screen,
                self.WHITE,
                (self.screen_width // 2, 0),
                (self.screen_width // 2, self.screen_height),
            )

            self.display_text(str(self.player1_score), self.screen_width // 4, 10)
            self.display_text(str(self.player2_score), self.screen_width * 3 // 4, 10)

            if self.paused:
                self.display_text(
                    "Paused", self.screen_width // 2 - 50, self.screen_height // 2 - 50
                )

            if game_over:
                self.display_text(
                    f"{winner} wins!",
                    self.screen_width // 2 - 100,
                    self.screen_height // 2 - 50,
                )
                self.display_text(
                    "Game Over", self.screen_width // 2 - 80, self.screen_height // 2
                )

                pygame.display.flip()

                pygame.time.delay(3000)

                self.player1_score = 0
                self.player2_score = 0
                self.reset_ball()
                game_over = False

            pygame.display.flip()

            self.clock.tick(self.frame_rate)


if __name__ == "__main__":
    pong_game = PongGame(
        screen_width=800,
        screen_height=600,
        paddle_width=20,
        paddle_height=100,
        paddle_speed=5,
        ball_size=20,
        ball_speed=3,
        winning_score=5,
        frame_rate=60,
    )
    pong_game.play()
