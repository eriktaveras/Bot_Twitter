from twython import Twython
import random

APP_KEY        = '9bizgXU1GlKdbSWKERHSrCYWH'
APP_SECRET     = 'tUzrftd3d9BxJ7IZMEcuzK4WdWIMj0tYaa92w1CKXZUwY73Gl9'
OAUTH_TOKEN        = '1204769679484608513-PfS9ChXRfHLBlqudvQwc7YNdGy1zy5'
OAUTH_TOKEN_SECRET = 'maIyY3CkDu3WCnOmlqv6yCUgaMcr5qcTCDtNacTeMK4gq'


twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


messages = [
     'Agua que no has de beber déjala correr',
     'A Dios rogando y con el mazo dando',
     'A caballo regalao no se le mira el diente',
     'Barriga llena, corazón contento',
     'Dios los crió y el diablo los juntó',
     'Está como abeja de piedra',
     'Está como ají-tití',
     'El que mucho abarca poco aprieta',
     'El burro sabe a quien tumba y el diablo a quien se lleva',
     'En casa de herrero, asadón de palo.',
     'Al que madruga Dios lo ayuda',
     'El que siembra en tierra ajena pierde el fruto y la semilla',
     'El que viste de lo ajeno en la calle lo desnudan',
     'El que de su falda corta las nalgas, cortas las nalgas enseña',
     'El que su caballo vende es porque muerde o patea',
     'El puerco cimarrón sabe en que palo se rasca',
     'El hombre precavido vale por dos',
     'El que da lo que tiene a pedir se queda',
     'Lo que hace con las manos lo desbarata con los pies',
     'Los dedos de la mano no son iguales',
     'Lo que tú no quieres para ti no lo desees para el otro',
     'La lengua es el castigo del cuerpo',
    ' La yagua que está para uno no se la comen los burros',
     'La mujer como el caballo se busca por la raza',
    ' La oveja se mama su teta y la ajena',
     'Lo quiere como la mula a la carreta',
     'Le tienen medio como el diablo a la cruz',
     'Más cuesta la sal que el chivo',
     'Más vale pájaro en mano que cientos volando',
     'Más vale malo conocido que bueno por conocer',
     'Más sabe el diablo por viejo que por diablo',
     'Más sabe el que quiere que el que puede',
     'Muerto que no hace ruido más grande son sus penas',
     'Nadie sabe lo que tiene hasta que no lo pierde',
     'No se deja camino real por vereda',
     'No ensucies el agua que vas a beber',
     'No dejes para mañana lo que puedes hacer hoy',
    ' No des consejo a quien no te lo pide',
     'No se cambia caballo a la mitad del río',
     'Puerco que no grita, cuchillo con el',
     'Paga lo que debes y sabrás lo que te queda',
     'Patada de yegua no duele',
     'Sancocho que usted no vaya a comer déjelo hervir',
     'Se hizo el chivo loco',
     'Tanto da la gotera en la piedra hasta que hace el hoyo',
     'Va como honda que lleva el diablo',
     'Yo no soy baúl de nadie',
     'Y é fácil?',
     'Los tropezones hacen levantar los pies'
   
]

message = random.choice(messages)

twitter.update_status(status=message)

