from time import sleep
from game import constants
from game.words import Words
from asciimatics.event import KeyboardEvent
from game.buffer import Buffer

class Director:
    def __init__(self, input_service, output_service, screen):
        
        self._screen = screen
        self._keep_playing = True
        self._input_service = input_service
        self._output_service = output_service
        self._words = Words
        self._buffer = Buffer

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
 
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        self.letter = self._input_service.get_letter()
        self._buffer.print_buffer(self.letter)

    def _do_updates(self):
        self._output_service.clear_screen()
        if self.letter == chr(13):
           self._words.check_word()
           self._buffer.clear_buffer()
        self._output_service.flush_buffer()

    def _do_outputs(self):
        pass
