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