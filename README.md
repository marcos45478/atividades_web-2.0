Sistema de Login com Flask
Sobre o Projeto

Este projeto é um sistema simples de login desenvolvido utilizando Python com Flask, HTML e CSS.

O objetivo principal foi praticar:

Integração do Flask com páginas HTML

Organização de arquivos estáticos (CSS)

Sistema básico de autenticação

Controle de tentativas de login

Funcionalidades

Tela de login

Validação de usuário e senha

Mensagens de erro para login inválido

Tentativa de implementar limite de tentativas de login

Problema Encontrado

Durante o desenvolvimento, tentei implementar um sistema de limite de tentativas de login, porém o sistema não estava funcionando corretamente.

O erro identificado foi que o arquivo login.css não estava sendo carregado corretamente pelo Flask.

O Flask não estava fazendo o bind (vinculação) correta do arquivo CSS, pois:

O arquivo não estava sendo puxado da pasta static

Ou o caminho no HTML estava incorreto
