class Scene:
    def initialization(self):
        '''Called in the constructor, to create a scene's variables that
        we can't really consider "attributes".
        '''
        ...

    def update_internal_variables(self):
        '''To update the internal variables of a scene such as entities,
        rects, etc...
        '''
        ...

    def event_loop(self):
        '''Handling all pygame events such as user inputs'''
        ...

    def display(self):
        '''Contains all display related functions such as screen-fills,
        blitting, etc...'''
        ...
