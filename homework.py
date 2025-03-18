import pygame

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame Window")

# Load an image
image = pygame.image.load("your_image.png")  # Replace with your image path
image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional)
    screen.fill((0, 0, 0))  # Black background

    # Draw the image on the screen
    screen.blit(image, image_rect)

    # Update display
    pygame.display.flip()

pygame.quit()
