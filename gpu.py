import time


class SimpleGpu:
    def __init__(self):
        import pygame
        import mem
        self.ram = mem.SimpleMem()
        self.pygame = pygame
        self.index = 10
        self.resulution = (600, 450)  # x, y
        self.pixel_color_white = (255, 255, 255)
        self.pixel_color_black = (0, 0, 0)
        pygame.init()
        self.window = pygame.display.set_mode((self.resulution[0], self.resulution[1]))
        self.font = pygame.font.Font(None, 20)



    def show_text(self, text, space=10):
        font = self.pygame.font.Font(None, 20)
        text_lable = font.render(text, False, 'WHITE')
        self.window.blit(text_lable, (space, self.index))
        self.pygame.display.flip()
        self.index += 15

    def show_text2(self, text, ram, format,space=10):
        text = text.removeprefix('"').removesuffix('"')
        font = self.pygame.font.Font(None, 20)


        def generate_range(min_value, max_value):
            min_value = int(min_value, 16) if min_value.isnumeric() else int(min_value, 16)
            max_value = int(max_value, 16) if max_value.isnumeric() else int(max_value, 16)
            result = [hex(i)[2:].upper() for i in range(min_value, max_value + 1)]
            return result

        if format == 'T':
            text_lable = font.render(text, False, 'WHITE')
            self.window.blit(text_lable, (space, self.index))
            self.pygame.display.flip()
            self.index += 15

        elif format == 'V':
            var_min = ram.map[text]['min']
            var_max = ram.map[text]['max']
            var_indexes = generate_range(var_min, var_max)
            xtext = ''
            for index in var_indexes:
                index = ram.index.index(index)
                xtext += chr(ram.ram[index])
            xtext = xtext.replace(chr(0x00), '')
            text_lable = font.render(xtext, False, 'WHITE')
            self.window.blit(text_lable, (space, self.index))
            self.pygame.display.flip()
            self.index += 15

        elif format == 'VR':
            var_min = ram.map[text]['min']
            var_max = ram.map[text]['max']
            var_indexes = generate_range(var_min, var_max)
            text_raw = ''
            for index in var_indexes:
                index = ram.index.index(index)
                text_raw += str(hex(ram.ram[index]))[2:]
                text_raw += ' '
            text_lable = font.render(text_raw, False, 'WHITE')
            self.window.blit(text_lable, (space, self.index))
            self.pygame.display.flip()
            self.index += 15
        else:
            text_lable = font.render(text, False, 'WHITE')
            self.window.blit(text_lable, (space, self.index))
            self.pygame.display.flip()
            self.index += 15

    def clear_screen(self):
        self.window.fill(self.pixel_color_black)
        self.pygame.display.flip()

    def update(self):
        self.pygame.display.flip()

    def IN(self, var, ram, question=''):
        space = 10
        input_text = ""
        question = question.removeprefix('"').removesuffix('"')
        font = self.pygame.font.Font(None, 20)
        while True:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    self.pygame.quit()
                elif event.type == self.pygame.KEYDOWN:
                    if event.key == self.pygame.K_RETURN:

                        def generate_range(min_value, max_value):
                            min_value = int(min_value, 16) if min_value.isnumeric() else int(min_value, 16)
                            max_value = int(max_value, 16) if max_value.isnumeric() else int(max_value, 16)
                            result = [hex(i)[2:].upper() for i in range(min_value, max_value + 1)]
                            return result

                        #print(ram.map)
                        var_min = ram.map[var]['min']
                        var_max = ram.map[var]['max']
                        var_indexes = generate_range(var_min, var_max)
                        #user_input = input(question)
                        if len(input_text) > len(var_indexes):
                            input_text = input_text[:len(var_indexes)]

                        for i in range(len(var_indexes)):
                            index = ram.index.index(var_indexes[i])
                            try:
                                ram.ram[index] = ord(input_text[i])
                            except IndexError:
                                ram.ram[index] = 0x00

                        self.index += 15
                        return None

                    elif event.key == self.pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

            rect = self.pygame.Rect(space, self.index, self.resulution[0],font.get_height()+1)
            self.window.fill((0, 0, 0), rect)
            text_lable = font.render(question+input_text, False, 'WHITE')
            self.window.blit(text_lable, (space, self.index))
            self.pygame.display.flip()

    def boot(self):
        font = self.pygame.font.Font(None, 20)
        text_lable = font.render('Booting image...', False, 'WHITE')
        self.window.blit(text_lable, (10, self.index))
        self.pygame.display.flip()
        time.sleep(2)
        self.window.fill(self.pixel_color_black)
        self.pygame.display.flip()


