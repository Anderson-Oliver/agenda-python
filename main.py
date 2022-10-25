from PyQt5 import uic,QtWidgets



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