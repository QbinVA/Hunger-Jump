import pygame

class Button:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color, hover_effect=True, border_color=None):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.border_color = border_color
        self.text = self.render_text_with_border(self.text_input, self.base_color)
        self.hover_effect = hover_effect

        # Si no hay imagen, usamos solo el texto
        if self.image is None:
            self.image = self.text
        self.original_image = self.image
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def render_text_with_border(self, text, color):
        """Renderiza texto con un borde si `border_color` está definido."""
        # Renderiza el texto principal
        text_surface = self.font.render(text, True, color)
        if self.border_color:
            # Tamaño del borde (ajustable si se requiere)
            border_size = 2

            # Crear una superficie transparente para el texto con borde
            border_surface = pygame.Surface(
                (text_surface.get_width() + 2 * border_size, text_surface.get_height() + 2 * border_size),
                pygame.SRCALPHA
            )

            # Dibujar el texto con el color del borde en varias posiciones
            for dx in range(-border_size, border_size + 1):
                for dy in range(-border_size, border_size + 1):
                    if dx != 0 or dy != 0:  # Solo bordes
                        border_surface.blit(self.font.render(text, True, self.border_color), (dx + border_size, dy + border_size))

            # Poner el texto principal encima
            border_surface.blit(text_surface, (border_size, border_size))
            return border_surface
        else:
            return text_surface

    def update(self, screen):
        """Dibuja el botón en la pantalla."""
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        """Verifica si el cursor está dentro del botón."""
        return self.rect.collidepoint(position)

    def changeColor(self, position):
        """Cambia el color del texto cuando el cursor está sobre el botón."""
        if self.checkForInput(position):
            self.text = self.render_text_with_border(self.text_input, self.hovering_color)
        else:
            self.text = self.render_text_with_border(self.text_input, self.base_color)

    def hoverEffect(self, position):
        """Aplica un efecto de hover (escala) al botón si está habilitado."""
        if self.hover_effect and self.checkForInput(position):
            # Aumentar el tamaño de la imagen
            self.image = pygame.transform.scale(
                self.original_image,
                (int(self.rect.width * 1.1), int(self.rect.height * 1.1))
            )
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        else:
            # Restaurar la imagen original
            self.image = self.original_image
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
