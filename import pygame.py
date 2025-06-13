import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 1000
HEIGHT = 700
UI_HEIGHT = 120
CANVAS_HEIGHT = HEIGHT - UI_HEIGHT

# Enhanced Color Palette
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
GRAY = (245, 245, 250)
DARK_GRAY = (180, 180, 190)
ACCENT = (74, 144, 226)
LIGHT_BLUE = (220, 235, 255)

# Beautiful drawing colors
COLORS = [
    (255, 75, 75),    # Red
    (75, 200, 75),    # Green
    (75, 150, 255),   # Blue
    (255, 200, 50),   # Yellow
    (255, 120, 200),  # Pink
    (150, 100, 255),  # Purple
    (255, 150, 75),   # Orange
    (50, 200, 200),   # Cyan
    (30, 30, 30),     # Black
    (120, 80, 60),    # Brown
]

MODES = ["titik", "garis", "draw", "persegi", "lingkaran", "elips"]

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("✨ Aplikasi Gambar Digital - Computer Graphics 24/25")

# Canvas
canvas = pygame.Surface((WIDTH, CANVAS_HEIGHT))
canvas.fill(WHITE)

# Fonts - using system fonts to avoid issues
try:
    font_title = pygame.font.Font(None, 24)
    font_normal = pygame.font.Font(None, 20)
    font_button = pygame.font.Font(None, 18)
except:
    font_title = pygame.font.SysFont('Arial', 24)
    font_normal = pygame.font.SysFont('Arial', 20)
    font_button = pygame.font.SysFont('Arial', 18)

def draw_text(text, pos, color=BLACK, font=None, bold=False):
    if font is None:
        font = font_normal
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, pos)

def draw_gradient_rect(surface, color1, color2, rect):
    """Draw a gradient rectangle"""
    for y in range(rect.height):
        blend = y / rect.height
        r = int(color1[0] * (1 - blend) + color2[0] * blend)
        g = int(color1[1] * (1 - blend) + color2[1] * blend)
        b = int(color1[2] * (1 - blend) + color2[2] * blend)
        pygame.draw.line(surface, (r, g, b), 
                        (rect.x, rect.y + y), 
                        (rect.x + rect.width, rect.y + y))

def draw_shadow_rect(surface, color, rect, shadow_offset=3):
    """Draw rectangle with shadow effect"""
    shadow_rect = rect.copy()
    shadow_rect.x += shadow_offset
    shadow_rect.y += shadow_offset
    pygame.draw.rect(surface, (200, 200, 200), shadow_rect, border_radius=10)
    pygame.draw.rect(surface, color, rect, border_radius=10)

# UI Elements positions and setup
color_start_x = 20
color_y = 97  # Turunkan posisi warna
circle_radius = 18
color_spacing = 45

# Create color circles with better positioning
color_circles = []
for i, color in enumerate(COLORS):
    x = color_start_x + i * color_spacing
    circle_rect = pygame.Rect(x - circle_radius, color_y - circle_radius, 
                             circle_radius * 2, circle_radius * 2)
    color_circles.append((circle_rect, color))

# Mode buttons with better styling
mode_start_x = 500
mode_y = 15  # Naikkan sedikit posisi tombol mode
button_width = 75  # Kecilkan sedikit untuk muat 6 tombol
button_height = 35
button_spacing = 80

mode_buttons = []
for i, mode in enumerate(MODES):
    x = mode_start_x + (i % 3) * button_spacing  # 3 tombol per baris
    if i < 3:
        y = mode_y
    else:
        y = mode_y + 45  # Baris kedua
    button_rect = pygame.Rect(x, y, button_width, button_height)
    mode_buttons.append((button_rect, mode))

# Enhanced clear button
clear_button = pygame.Rect(WIDTH - 140, 15, 110, 35)
save_button = pygame.Rect(WIDTH - 140, 55, 110, 30)

# State variables
current_mode = 0
current_color_index = 0
drawing = False
start_pos = None
current_pos = None
draw_points = []  # Untuk mode draw bebas

# Animation variables
button_hover = -1
color_hover = -1
clear_hover = False
save_hover = False

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    mouse_pos = pygame.mouse.get_pos()
    
    # Check hover states
    button_hover = -1
    color_hover = -1
    clear_hover = clear_button.collidepoint(mouse_pos)
    save_hover = save_button.collidepoint(mouse_pos)
    
    for i, (rect, _) in enumerate(mode_buttons):
        if rect.collidepoint(mouse_pos):
            button_hover = i
            break
    
    for i, (circle_rect, _) in enumerate(color_circles):
        if circle_rect.collidepoint(mouse_pos):
            color_hover = i
            break
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Color selection
            for i, (circle_rect, _) in enumerate(color_circles):
                if circle_rect.collidepoint(mouse_pos):
                    current_color_index = i

            # Mode selection
            for i, (button_rect, _) in enumerate(mode_buttons):
                if button_rect.collidepoint(mouse_pos):
                    current_mode = i

            # Clear button
            if clear_button.collidepoint(mouse_pos):
                canvas.fill(WHITE)

            # Save button (placeholder)
            if save_button.collidepoint(mouse_pos):
                pygame.image.save(canvas, "gambar_saya.png")

            # Canvas drawing
            if mouse_pos[1] > UI_HEIGHT:
                drawing = True
                start_pos = (mouse_pos[0], mouse_pos[1] - UI_HEIGHT)
                current_pos = start_pos
                
                if MODES[current_mode] == "titik":
                    pygame.draw.circle(canvas, COLORS[current_color_index], start_pos, 3)
                elif MODES[current_mode] == "draw":
                    draw_points = [start_pos]  # Mulai list titik untuk draw bebas

        elif event.type == pygame.MOUSEMOTION and drawing:
            current_pos = (event.pos[0], event.pos[1] - UI_HEIGHT)
            
            # Untuk mode draw, tambahkan titik ke list dan gambar langsung
            if MODES[current_mode] == "draw":
                draw_points.append(current_pos)
                if len(draw_points) > 1:
                    pygame.draw.line(canvas, COLORS[current_color_index], 
                                   draw_points[-2], draw_points[-1], 3)

        elif event.type == pygame.MOUSEBUTTONUP and drawing:
            # Untuk mode draw, tidak perlu gambar lagi karena sudah digambar saat motion
            if MODES[current_mode] != "draw":
                end_pos = (event.pos[0], event.pos[1] - UI_HEIGHT)
                mode = MODES[current_mode]
                color = COLORS[current_color_index]

                if mode == "garis":
                    pygame.draw.line(canvas, color, start_pos, end_pos, 3)
                elif mode == "persegi":
                    rect = pygame.Rect(*start_pos, end_pos[0]-start_pos[0], end_pos[1]-start_pos[1])
                    pygame.draw.rect(canvas, color, rect, 3)
                elif mode == "lingkaran":
                    radius = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2)**0.5)
                    if radius > 0:
                        pygame.draw.circle(canvas, color, start_pos, radius, 3)
                elif mode == "elips":
                    rect = pygame.Rect(*start_pos, end_pos[0]-start_pos[0], end_pos[1]-start_pos[1])
                    if rect.width != 0 and rect.height != 0:
                        pygame.draw.ellipse(canvas, color, rect, 3)

            drawing = False
            start_pos = None
            current_pos = None
            draw_points = []  # Reset points untuk draw bebas

    # Draw beautiful UI background
    draw_gradient_rect(screen, LIGHT_BLUE, GRAY, pygame.Rect(0, 0, WIDTH, UI_HEIGHT))
    
    # Draw decorative line
    pygame.draw.line(screen, ACCENT, (0, UI_HEIGHT-2), (WIDTH, UI_HEIGHT-2), 3)
    
    # Title and current mode display
    title_surface = font_title.render("🎨 Digital Art Studio", True, ACCENT)
    screen.blit(title_surface, (20, 15))
    
    mode_surface = font_normal.render(f"Mode: {MODES[current_mode].upper()}", True, BLACK)
    screen.blit(mode_surface, (20, 40))
    
    # Color palette with enhanced styling
    color_label = font_button.render("Palet Warna:", True, BLACK)
    screen.blit(color_label, (20, 58))
    for i, (circle_rect, color) in enumerate(color_circles):
        # Shadow effect for colors
        shadow_pos = (circle_rect.centerx + 2, circle_rect.centery + 2)
        pygame.draw.circle(screen, (200, 200, 200), shadow_pos, circle_radius)
        
        # Main color circle
        pygame.draw.circle(screen, color, circle_rect.center, circle_radius)
        
        # Selection indicator
        if i == current_color_index:
            pygame.draw.circle(screen, WHITE, circle_rect.center, circle_radius + 4, 3)
            pygame.draw.circle(screen, BLACK, circle_rect.center, circle_radius + 4, 1)
        
        # Hover effect
        if i == color_hover:
            pygame.draw.circle(screen, (255, 255, 255, 100), circle_rect.center, circle_radius + 2, 2)

    # Enhanced mode buttons
    for i, (rect, name) in enumerate(mode_buttons):
        if i == current_mode:
            # Active button
            draw_shadow_rect(screen, ACCENT, rect)
            text_color = WHITE
        elif i == button_hover:
            # Hover effect
            draw_shadow_rect(screen, (100, 180, 255), rect)
            text_color = WHITE
        else:
            # Normal button
            draw_shadow_rect(screen, WHITE, rect)
            text_color = BLACK
        
        # Button border
        pygame.draw.rect(screen, DARK_GRAY, rect, 1, border_radius=10)
        
        # Button text
        text_surface = font_button.render(name.capitalize(), True, text_color)
        text_rect = text_surface.get_rect()
        text_x = rect.centerx - text_rect.width // 2
        text_y = rect.centery - text_rect.height // 2
        screen.blit(text_surface, (text_x, text_y))

    # Enhanced clear button
    clear_color = (255, 100, 100) if clear_hover else (255, 80, 80)
    draw_shadow_rect(screen, clear_color, clear_button)
    pygame.draw.rect(screen, (200, 50, 50), clear_button, 2, border_radius=10)
    clear_text = font_button.render("🗑️ Hapus", True, WHITE)
    screen.blit(clear_text, (clear_button.x + 15, clear_button.y + 10))

    # Save button
    save_color = (100, 200, 100) if save_hover else (80, 180, 80)
    draw_shadow_rect(screen, save_color, save_button)
    pygame.draw.rect(screen, (50, 150, 50), save_button, 2, border_radius=10)
    save_text = font_button.render("💾 Simpan", True, WHITE)
    screen.blit(save_text, (save_button.x + 10, save_button.y + 5))

    # Canvas with border
    canvas_rect = pygame.Rect(0, UI_HEIGHT, WIDTH, CANVAS_HEIGHT)
    pygame.draw.rect(screen, (220, 220, 220), canvas_rect, 2)
    screen.blit(canvas, (0, UI_HEIGHT))

    # Preview while drawing with enhanced visuals
    if drawing and current_pos and MODES[current_mode] != "draw":
        preview_color = (*COLORS[current_color_index][:3], 150)  # Semi-transparent
        
        if MODES[current_mode] == "garis":
            pygame.draw.line(screen, COLORS[current_color_index],
                           (start_pos[0], start_pos[1] + UI_HEIGHT),
                           (current_pos[0], current_pos[1] + UI_HEIGHT), 2)
        elif MODES[current_mode] == "persegi":
            rect = pygame.Rect(start_pos[0], start_pos[1] + UI_HEIGHT,
                             current_pos[0] - start_pos[0], current_pos[1] - start_pos[1])
            pygame.draw.rect(screen, COLORS[current_color_index], rect, 2)
        elif MODES[current_mode] == "lingkaran":
            radius = int(((current_pos[0]-start_pos[0])**2 + (current_pos[1]-start_pos[1])**2)**0.5)
            if radius > 0:
                pygame.draw.circle(screen, COLORS[current_color_index],
                                 (start_pos[0], start_pos[1] + UI_HEIGHT), radius, 2)
        elif MODES[current_mode] == "elips":
            rect = pygame.Rect(start_pos[0], start_pos[1] + UI_HEIGHT,
                             current_pos[0] - start_pos[0], current_pos[1] - start_pos[1])
            if rect.width != 0 and rect.height != 0:
                pygame.draw.ellipse(screen, COLORS[current_color_index], rect, 2)

    # Status bar
    status_text = f"Ukuran: {WIDTH}x{CANVAS_HEIGHT} | Warna: RGB{COLORS[current_color_index]} | Tool: {MODES[current_mode].upper()}"
    status_surface = font_button.render(status_text, True, DARK_GRAY)
    screen.blit(status_surface, (20, HEIGHT - 25))

    pygame.display.flip()
    clock.tick(60)  # 60 FPS for smooth animations

pygame.quit()
sys.exit()