from PyQt5 import uic,QtWidgets


def chama_tela_login():
    TelaLogin.show()
    TelaPrincipal.close()

def chama_tela_usuario():
    TelaUsuario.show()
    TelaPrincipal.close()

def chama_tela_principal():
    TelaPrincipal.show()
    TelaUsuario.close()
    TelaPessoa.close()

def chama_tela_pessoa():
    TelaPessoa.show()
    TelaPrincipal.close()

app=QtWidgets.QApplication([])

TelaLogin=uic.loadUi('TelaLogin.ui')
TelaPrincipal=uic.loadUi('TelaPrincipal.ui')
TelaUsuario=uic.loadUi('TelaUsuario.ui')
TelaPessoa=uic.loadUi('TelaPessoa.ui')

TelaPrincipal.btnCadUser.clicked.connect(chama_tela_usuario)
TelaPrincipal.btnCadPessoa.clicked.connect(chama_tela_pessoa)
TelaPrincipal.btnVoltar.clicked.connect(chama_tela_login)

TelaUsuario.btnVoltar.clicked.connect(chama_tela_principal)

TelaPessoa.btnVoltar.clicked.connect(chama_tela_principal)

TelaPrincipal.show()
app.exec()