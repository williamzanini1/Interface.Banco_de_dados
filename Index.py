import sys
from time import sleep 
import os
import pygame
import sqlite3
import pandas as pd
import platform
from getpass import getpass
from tkinter import *
from tkinter import messagebox
import customtkinter


conexao = sqlite3.connect('passageiros.db')

def dadosP():

    conexao = sqlite3.connect('passageiros.db')
    
    c = conexao.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS passageiros (
        nome text,
        telefone,
        cpf text,
        idade text,
        genero text
        )
    ''')


    cpf = entry_CPF.get()
    Fone = entry_fone.get()
    Name = entry_nome.get()
    genero = entry_genero.get()


    try:   
        Fone = int(entry_fone.get())

    except UnboundLocalError:
        messagebox.showerror(title="ERRO", message="Preencha o telefone apenas com números")   
    except ValueError:
        messagebox.showerror(title="ERRO", message="Preencha o telefone apenas com números")
    except NameError:
        messagebox.showerror(title="ERRO", message="Preencha o telefone apenas com números")
    except TypeError:
        messagebox.showerror(title="ERRO", message="Preencha o telefone apenas com números")              
    else:
        pass

    try:   
        cpf = int(entry_CPF.get())

    except UnboundLocalError:
        messagebox.showerror(title="ERRO", message="Preencha os oito números do seu CPF")   
    except ValueError:
        messagebox.showerror(title="ERRO", message="Preencha os oito números do seu CPF")
    except NameError:
        messagebox.showerror(title="ERRO", message="Preencha os oito números do seu CPF")
    except TypeError:
        messagebox.showerror(title="ERRO", message="Preencha os oito números do seu CPF")
    else:
        pass                  

    if (genero in "masculino"  or genero  in "feminino"  or genero  in "trans"):
        pass
        
                    

        c.execute("INSERT INTO passageiros VALUES (:nome, :telefone, :cpf, :idade, :genero)",
                    {
                    'nome':entry_nome.get(),
                    'telefone' :entry_fone.get(),
                    'cpf' :entry_CPF.get(),
                    'idade' :entry_idade.get(),
                    'genero' :entry_genero.get()
                    }
                    )
        

        conexao.commit()

        conexao.close()

        entry_nome.delete(0, 'end')
        entry_CPF.delete(0, 'end')
        entry_idade.delete(0, 'end')
        entry_genero.delete(0, 'end')
        entry_fone.delete(0, 'end')
    
        messagebox.showinfo(title="Register Info", message="Accont Create!")
    
    else:
        messagebox.showerror(title="ERRO", message="Em genero digite masculino, feminino ou trans")

        conexao.commit()

        conexao.close()


def exportarP():

    conexao = sqlite3.connect('passageiros.db')

    c = conexao.cursor()
    
    c.execute("SELECT*, oid FROM passageiros")
    cadastrados = c.fetchall()
    cadastrados = pd.DataFrame(cadastrados, columns=['nome', 'telefone', 'cpf', 'idade', 'genero', 'ID_Banco'])
    cadastrados.to_excel('Passageiros.xlsx')
    messagebox.showinfo(title='EXPORT', message= 'DADOS EXPORTADOS!') 
            
    conexao.commit()

    conexao.close()


def exportarT():

    conexao = sqlite3.connect('tripulantes.db')

    c = conexao.cursor()

    c.execute("SELECT*, oid FROM tripulantes")
    cadastrados = c.fetchall()
    cadastrados = pd.DataFrame(cadastrados, columns=['nome', 'cracha', 'senha', 'ID_Banco'])
    cadastrados.to_excel('tripulantes.xlsx')
    messagebox.showinfo(title='EXPORT', message= 'DADOS EXPORTADOS!') 
            
    conexao.commit()

    conexao.close()



conexao = sqlite3.connect('tripulantes.db')



def dadosT():

    global userL
    global senhaL
    global NameT
    global CrachaT
    global Pass1
    global Pass2

    NameT = nome.get()
    CrachaT = cracha1.get()
    Pass2 = senha2.get()
    Pass1 = senha1.get()

    conexao = sqlite3.connect('tripulantes.db')

    c = conexao.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS tripulantes (
        nome text,
        cracha text,
        senha text
        )
    ''')


    if Pass2 != Pass1:
            messagebox.showerror(title="ERRO", message="As senhas não combinam")
    else:

        if (NameT == '' or CrachaT == '' or Pass2 == '' or Pass1 =="" ):
            messagebox.showerror(title="Erro", message="Preencha todos os campos")
        else:

            try:    
                NameT = str(userL.get())
            except ValueError:
                messagebox.showerror(title="ERRO", message="Preencha corretamente")
            except NameError:
                messagebox.showerror(title="ERRO", message="Preencha corretamente")
            except TypeError:
                messagebox.showerror(title="ERRO", message="Preencha corretamente")
            except KeyError:
                messagebox.showerror(title="ERRO", message="Preencha corretamente")
            else:
                            
                try:    
                    Pass2 = int(senha2.get())                  
                except ValueError:
                    messagebox.showerror(title="ERRO", message="Preencha a senha com números")
                except NameError:
                    messagebox.showerror(title="ERRO", message="Preencha a senha com números")
                except TypeError:
                    messagebox.showerror(title="ERRO", message="Preencha a senha com números")
                except KeyError:
                    messagebox.showerror(title="ERRO", message="Preencha a senha com números")                 
                else:

                    try:    
                        CrachaT = int(cracha1.get())                  
                    except ValueError:
                        messagebox.showerror(title="ERRO", message="Preencha o número do crachá corretamente")
                    except NameError:
                        messagebox.showerror(title="ERRO", message="Preencha o número do crachá corretamente")
                    except TypeError:
                        messagebox.showerror(title="ERRO", message="Preencha o número do crachá corretamente")
                    except KeyError:
                        messagebox.showerror(title="ERRO", message="Preencha o número do crachá corretamente")                 
                    else:
                

                        c.execute("INSERT INTO tripulantes VALUES (:nome, :cracha, :senha)",
                                {
                                'nome':nome.get(),
                                'cracha' :cracha1.get(),
                                'senha' :senha2.get()
                                }
                                )

                        conexao.commit()

                        conexao.close()

                        nome.delete(0, 'end')
                        cracha1.delete(0, 'end')
                        senha1.delete(0, 'end')
                        senha2.delete(0, 'end')
                            
                        messagebox.showinfo(title="Register Info", message="Passageiro cadastrado!")

def login():

    conexao = sqlite3.connect('tripulantes.db')

    c =  conexao.cursor()

    User = userL.get()
    Pass = senhaL.get()

    c.execute("""
    SELECT * FROM tripulantes 
    WHERE (cracha = ? and senha = ?) 
    """, (User, Pass))

    verify = c.fetchone()

    try:
        if (User in verify and Pass in verify):
            messagebox.showinfo(title="Acess", message= "WELCOME!")
            janela.destroy()
            cadastrarpass()
    except:
        messagebox.showinfo(title="ERRO", message="Usuário ou senha incorreto's")

        conexao.commit()

        conexao.close()


def cadastrarpass():

    global entry_nome
    global entry_idade
    global entry_genero
    global entry_CPF
    global entry_fone

    janela = customtkinter.CTk()

    janela.geometry('500x500')
    janela.resizable(True, True)
    janela.title('CADATRAR PASSAGEIROS')
    
    pastaApp=os.path.dirname(__file__)
    imagem = PhotoImage(file=pastaApp+'\\Titanic2.png')
    logo = Label(image=imagem)
    logo.place(x=10, y=10)

    entry_nome = customtkinter.CTkEntry(janela, placeholder_text='NOME COMPLETO')
    entry_nome.pack(padx=10, pady=10)

    entry_fone = customtkinter.CTkEntry(janela, placeholder_text='TELEFONE')
    entry_fone.pack(padx=10, pady=10)

    entry_CPF = customtkinter.CTkEntry(janela, placeholder_text='CPF')
    entry_CPF .pack(padx=10, pady=10)

    entry_idade = customtkinter.CTkEntry(janela, placeholder_text='IDADE')
    entry_idade.pack(padx=10, pady=10)

    entry_genero = customtkinter.CTkEntry(janela, placeholder_text='GENERO')
    entry_genero.pack(padx=10, pady=10)
    
    botão = customtkinter.CTkButton(janela, text='CADASTRAR', command= dadosP)
    botão.pack(padx =10, pady=10)

    botão = customtkinter.CTkButton(janela, text='EXPORTAR', command= exportarP)
    botão.pack(padx =10, pady=10)

    janela.mainloop()



def cadastrartrip():

    global nome
    global cracha1
    global senha1
    global senha2

    janela = customtkinter.CTk()

    janela.geometry('500x500')
    janela.resizable(True, True)
    janela.title('CADATRAR TRIPULANTE')
    
    pastaApp=os.path.dirname(__file__)
    imagem = PhotoImage(file=pastaApp+'\\Titanic2.png')
    logo = Label(image=imagem)
    logo.place(x=10, y=10)

    nome = customtkinter.CTkEntry(janela, placeholder_text='NOME')
    nome.pack(padx=10, pady=10)

    cracha1 = customtkinter.CTkEntry(janela, placeholder_text='CRACHÁ')
    cracha1.pack(padx=10, pady=10)    

    senha1 = customtkinter.CTkEntry(janela, placeholder_text='SENHA', show='*')
    senha1.pack(padx=10, pady=10)

    senha2 = customtkinter.CTkEntry(janela, placeholder_text='REPITA SENHA', show='*')
    senha2.pack(padx=10, pady=10)

    botãoL = customtkinter.CTkButton(janela, text='CADASTRAR', command= dadosT)
    botãoL.pack(padx =10, pady=10)

    botãoC = customtkinter.CTkButton(janela, text='EXPORTAR', command=exportarT)
    botãoC.pack(padx =10, pady=10)


    def fechar2():
       janela.destroy()
       
    botãoL = customtkinter.CTkButton(janela, text='FECHAR', command=fechar2)
    botãoL.pack(padx =10, pady=10)

    janela.mainloop()


janela = customtkinter.CTk()

janela.geometry('500x500')
janela.resizable(True, True)
janela.title('LOGIN')

pygame.init()
pygame.mixer.music.load('ex1.mp3')
pygame.mixer_music.play()
pygame.event.wait()

pastaApp=os.path.dirname(__file__)
imagem = PhotoImage(file=pastaApp+'\\Titanic2.png')
logo = Label(image=imagem)
logo.place(x=10, y=10)

userL = customtkinter.CTkEntry(janela, placeholder_text='CRACHÁ', show ='*')
userL.pack(padx=10, pady=10)

senhaL = customtkinter.CTkEntry(janela, placeholder_text='SENHA', show='*')
senhaL.pack(padx=10, pady=10)

botãoL = customtkinter.CTkButton(janela, text='LOGIN', command= login)
botãoL.pack(padx =10, pady=10)

def fechar():
    janela.destroy()
    cadastrartrip()

botãoC = customtkinter.CTkButton(janela, text='CADASTRAR', command=fechar)
botãoC.pack(padx =10, pady=10)

janela.mainloop()

