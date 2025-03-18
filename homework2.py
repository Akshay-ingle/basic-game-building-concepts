import pygame

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Basics")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set up fonts
font = pygame.font.Font(None, 36)

# Main loop
running = True
while running:
    screen.fill(WHITE)  # Fill background with white

    # Draw a polygon (triangle)
    pygame.draw.polygon(screen, BLUE, [(250, 100), (150, 300), (350, 300)])

    # Render text
    text = font.render("Hello, Pygame!", True, RED)
    screen.blit(text, (150, 50))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()  # Update the display

pygame.quit()
