class Question :

    def __init__(self , Pregunta , Respuesta , multipleChoiceOptions=None) :
        self.Pregunta = Pregunta
        self.Respuesta = Respuesta
        self.multipleChoiceOptions = multipleChoiceOptions

    def __repr__(self) :
        return '{' + self.Pregunta + ', ' + self.Respuesta + ', ' + str ( self.multipleChoiceOptions ) + '}'

    print ( "Question 1. What city is the capital of Australia?" )
    userInput = input (preguntas [ 0 ] [ 0 ] = "CATEGORÍA: GEOGRAFÍA ¿De qué país forma parte Hawaii?"
    preguntas [ 0 ] [ 1 ] = "[1] Estados Unidos"
    preguntas [ 0 ] [ 2 ] = "[2] Argentina"
    preguntas [ 0 ] [ 3 ] = "[3] Brasil"
    preguntas [ 0 ] [ 4 ] = "[4] Ecuador" )

    preguntas [ 0 ] [ 0 ] = "CATEGORÍA: GEOGRAFÍA ¿De qué país forma parte Hawaii?"
    preguntas [ 0 ] [ 1 ] = "[1] Estados Unidos"
    preguntas [ 0 ] [ 2 ] = "[2] Argentina"
    preguntas [ 0 ] [ 3 ] = "[3] Brasil"
    preguntas [ 0 ] [ 4 ] = "[4] Ecuador"
    preguntas [ 0 ] [ 5 ] = "1"
    preguntas [ 1 ] [ 0 ] = "CATEGORÍA: GEOGRAFÍA ¿Cuántos estados tiene integrados Estados Unidos?"
    preguntas [ 1 ] [ 1 ] = "49"
    preguntas [ 1 ] [ 2 ] = "15"
    preguntas [ 1 ] [ 3 ] = "50"
    preguntas [ 1 ] [ 4 ] = "180"
    preguntas [ 1 ] [ 5 ] = "3"
    preguntas [ 2 ] [ 0 ] = "CATEGORÍA: GEOGRAFÍA ¿De qué año es la Constitución Española?"
    preguntas [ 2 ] [ 1 ] = "1999"
    preguntas [ 2 ] [ 2 ] = "1978"
    preguntas [ 2 ] [ 3 ] = "1979"
    preguntas [ 2 ] [ 4 ] = "1845"
    preguntas [ 2 ] [ 5 ] = "2"
    preguntas [ 3 ] [ 0 ] = "CATEGORÍA: GEOGRAFÍA ¿Cuál es el río más largo de España?"
    preguntas [ 3 ] [ 1 ] = "El río Elbro"
    preguntas [ 3 ] [ 2 ] = "Opción 2"
    preguntas [ 3 ] [ 3 ] = "Opción 3"
    preguntas [ 3 ] [ 4 ] = "Opción 4"
    preguntas [ 3 ] [ 5 ] = "1"
    preguntas [ 4 ] [ 0 ] = "CATEGORÍA: GEOGRAFÍA ¿Cuál es el océano más grande del mundo?"
    preguntas [ 4 ] [ 1 ] = "El océano Atlántico"
    preguntas [ 4 ] [ 2 ] = "El océano Pacífico"
    preguntas [ 4 ] [ 3 ] = "El océano Índico"
    preguntas [ 4 ] [ 4 ] = "El océano Ártico"
    preguntas [ 4 ] [ 5 ] = "2"

    for question in quizQuestions :
        if (question.multipleChoiceOptions != None) :
            print ( f"{question.questionText}?" )
            for option in question.multipleChoiceOptions :
                print ( option )
            userInput = input ( )
        else :
            print ( f"{question.questionText}?" )
            userInput = input ( )

        if (userInput.lower ( ) == question.answer.lower ( )) :
            print ( "That is correct!" )
        else :
            print ( f"Sorry, the correct answer is {question.answer}." )