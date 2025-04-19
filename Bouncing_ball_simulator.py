import pygame
import sys

# Initialize pygame
pygame.init()

# Get screen dimensions dynamically
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball properties
ball_radius = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 0
ball_speed_y = 0

# Damping factor
damping = 0.99  # Adjust this value for faster/slower damping

# Gravity (reduced for lighter ball)
gravity = 0.2  # Adjust this value for stronger/weaker gravity

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Bouncing Ball Animation with Gravity")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Dragging state
dragging = False
drag_start_x, drag_start_y = 0, 0

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse is on the ball
            mouse_x, mouse_y = event.pos
            if (mouse_x - ball_x) ** 2 + (mouse_y - ball_y) ** 2 <= ball_radius ** 2:
                dragging = True
                drag_start_x, drag_start_y = mouse_x, mouse_y
                ball_speed_x, ball_speed_y = 0, 0  # Stop the ball while dragging
        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging:
                dragging = False
                # Calculate the velocity based on drag motion
                mouse_x, mouse_y = event.pos
                ball_speed_x = (mouse_x - drag_start_x) / 10  # Adjust divisor for sensitivity
                ball_speed_y = (mouse_y - drag_start_y) / 10
        elif event.type == pygame.MOUSEMOTION and dragging:
            # Update ball position to follow the mouse
            ball_x, ball_y = event.pos

    if not dragging:
        # Apply gravity
        ball_speed_y += gravity

        # Move the ball
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Apply damping to slow down the ball
        ball_speed_x *= damping
        ball_speed_y *= damping

        # Bounce the ball off the walls
        if ball_x - ball_radius < 0:
            ball_x = ball_radius
            ball_speed_x = -ball_speed_x
        elif ball_x + ball_radius > WIDTH:
            ball_x = WIDTH - ball_radius
            ball_speed_x = -ball_speed_x

        if ball_y - ball_radius < 0:
            ball_y = ball_radius
            ball_speed_y = -ball_speed_y
        elif ball_y + ball_radius > HEIGHT:
            ball_y = HEIGHT - ball_radius
            ball_speed_y = -ball_speed_y

    # Clear the screen
    screen.fill(BLACK)

    # Draw the ball
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
