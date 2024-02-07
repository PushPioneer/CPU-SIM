class SimpleGpu:
    def __init__(self):
        import pygame
        self.pygame = pygame

        self.pixel_size = 5
        self.resulution = (600, 450)  # x, y
        self.gpu_ram = [0] * 32
        self.line_buffer = [1] * self.resulution[0]
        self.frame_buffer = [0] * int(self.resulution[0] * self.resulution[1] / self.pixel_size)
        self.pixel_color_white = (255, 255, 255)
        self.pixel_color_black = (0, 0, 0)
        pygame.init()
        self.window = pygame.display.set_mode((self.resulution[0], self.resulution[1]))
        self.font = pygame.font.Font(None, 20)

    class index:
        def __init__(self):
            self.index = 10

    def show_text(self, text, index_class=index(), space=10):
        font = self.pygame.font.Font(None, 20)
        text_lable = font.render(text, False, 'WHITE')
        self.window.blit(text_lable, (space, index_class.index))
        self.pygame.display.flip()
        index_class.index += 15

    def clear_screen(self):
        self.window.fill(self.pixel_color_black)
        self.pygame.display.flip()

    def update(self):
        self.pygame.display.flip()

    def dump_linebuffer(self,line=0):
        for i in range(len(self.line_buffer)):
            if self.line_buffer[i] == 1:
                self.pygame.draw.rect(self.window, self.pixel_color_white, (i, line, self.pixel_size, self.pixel_size))
            else:
                self.pygame.draw.rect(self.window, self.pixel_color_black, (i, line, self.pixel_size, self.pixel_size))
        self.update()

    def dump_framebuffer(self):
        row_index = 0
        line_index = 0
        for pixel in self.frame_buffer:
            if pixel == 1:
                self.pygame.draw.rect(self.window, self.pixel_color_white, (row_index, line_index, self.pixel_size, self.pixel_size))
            else:
                self.pygame.draw.rect(self.window, self.pixel_color_black, (row_index, line_index, self.pixel_size, self.pixel_size))
            if row_index == self.resulution[0]:
                line_index += 5
                row_index = 0
            else:
                row_index += 5
        self.update()
