class InputBox:
    def __init__(self, pygame, label, x, y, w, h, text=''):
        self.pg = pygame
        self.COLOR_INACTIVE = self.pg.Color('black')
        self.COLOR_ACTIVE = self.pg.Color('dodgerblue2')
        self.color = self.COLOR_INACTIVE
        self.FONT = self.pg.font.Font("resources/fonts/Roboto.ttf", 32)
        self.LABEL_FONT = self.pg.font.Font("resources/fonts/Roboto.ttf", 18)
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.label = label
        self.label_surface = self.LABEL_FONT.render(label, True, self.pg.Color('black'))
        self.txt_surface = self.FONT.render(text, True, self.COLOR_INACTIVE)
        self.active = False

    def handle_event(self, event):
        if event.type == self.pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE
        if event.type == self.pg.KEYDOWN:
            if self.active:
                if event.key == self.pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == self.pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.FONT.render(self.text, True, self.COLOR_INACTIVE)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the label
        screen.blit(self.label_surface, (self.rect.x - len(self.label) * 12, self.rect.y + 7))
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        self.pg.draw.rect(screen, self.color, self.rect, 2)
