class Question :

    def __init__(self , Pregunta , Respuesta , multipleChoiceOptions=None) :
        self.Pregunta = Pregunta
        self.Respuesta = Respuesta
        self.multipleChoiceOptions = multipleChoiceOptions

    def __repr__(self) :
        return '{' + self.Pregunta + ', ' + self.Respuesta + ', ' + str ( self.multipleChoiceOptions ) + '}'

    print ( "Question 1. What city is the capital of Australia?" )
    userInput = (int(input(preguntas [ 0 ] [ 0 ] = "CATEGORÍA: GEOGRAFÍA ¿De qué país forma parte Hawaii?"))
    