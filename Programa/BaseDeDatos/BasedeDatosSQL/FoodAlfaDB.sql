PGDMP         *        	        {            FoodAlfa    15.4    15.4 <    M           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            N           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            O           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            P           1262    24576    FoodAlfa    DATABASE     }   CREATE DATABASE "FoodAlfa" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Chile.1252';
    DROP DATABASE "FoodAlfa";
                postgres    false            �            1259    24602    Empresas    TABLE     �   CREATE TABLE public."Empresas" (
    "IdEmpresa" bigint NOT NULL,
    "Empresa" text NOT NULL,
    "Identificacion" bigint NOT NULL,
    "IdLocal" bigint NOT NULL
);
    DROP TABLE public."Empresas";
       public         heap    postgres    false            �            1259    24601    Empresas_IdEmpresa_seq    SEQUENCE     �   ALTER TABLE public."Empresas" ALTER COLUMN "IdEmpresa" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Empresas_IdEmpresa_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
    CYCLE
);
            public          postgres    false    219            �            1259    24628    Estado    TABLE     ]   CREATE TABLE public."Estado" (
    "IdEstado" bigint NOT NULL,
    "Estado" text NOT NULL
);
    DROP TABLE public."Estado";
       public         heap    postgres    false            �            1259    24627    EstadoPedido_IdEstadoPedido_seq    SEQUENCE     �   ALTER TABLE public."Estado" ALTER COLUMN "IdEstado" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."EstadoPedido_IdEstadoPedido_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
    CYCLE
);
            public          postgres    false    223            �            1259    24622    Locales    TABLE     A   CREATE TABLE public."Locales" (
    "IdLocal" bigint NOT NULL
);
    DROP TABLE public."Locales";
       public         heap    postgres    false            �            1259    24621    Locales_IdLocal_seq    SEQUENCE     �   ALTER TABLE public."Locales" ALTER COLUMN "IdLocal" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Locales_IdLocal_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
    CYCLE
);
            public          postgres    false    221            �            1259    24636    Mesas    TABLE     R   CREATE TABLE public."Mesas" (
    "IdMesa" bigint NOT NULL,
    "Mesas" bigint
);
    DROP TABLE public."Mesas";
       public         heap    postgres    false            �            1259    24635    Mesas_IdMesa_seq    SEQUENCE     �   ALTER TABLE public."Mesas" ALTER COLUMN "IdMesa" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Mesas_IdMesa_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
    CYCLE
);
            public          postgres    false    225            �            1259    24650    Pedidos    TABLE     �   CREATE TABLE public."Pedidos" (
    "IdPedido" bigint NOT NULL,
    "Precio" bigint,
    "FechaYHora" timestamp with time zone,
    "IdMesa" bigint NOT NULL,
    "IdEstado" bigint NOT NULL,
    "IdMeseso" bigint NOT NULL
);
    DROP TABLE public."Pedidos";
       public         heap    postgres    false            �            1259    24649    Pedidos_IdPedido_seq    SEQUENCE     �   ALTER TABLE public."Pedidos" ALTER COLUMN "IdPedido" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Pedidos_IdPedido_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
    CYCLE
);
            public          postgres    false    229            �            1259    24642    Platos    TABLE     �   CREATE TABLE public."Platos" (
    "IdPlato" bigint NOT NULL,
    "NombrePlato" text NOT NULL,
    "Precio" bigint NOT NULL,
    "IdEmpresa" bigint
);
    DROP TABLE public."Platos";
       public         heap    postgres    false            �            1259    24641    Platos_IdPlato_seq    SEQUENCE     �   ALTER TABLE public."Platos" ALTER COLUMN "IdPlato" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Platos_IdPlato_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
    CYCLE
);
            public          postgres    false    227            �            1259    24578    Roles    TABLE     M   CREATE TABLE public."Roles" (
    "IdRol" bigint NOT NULL,
    "Rol" text
);
    DROP TABLE public."Roles";
       public         heap    postgres    false            �            1259    24577    Roles_IdRol_seq    SEQUENCE     �   ALTER TABLE public."Roles" ALTER COLUMN "IdRol" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Roles_IdRol_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 3
    CACHE 1
    CYCLE
);
            public          postgres    false    215            �            1259    24656 	   SubPedido    TABLE     �   CREATE TABLE public."SubPedido" (
    "IdSubPedido" bigint NOT NULL,
    "Cantidad" bigint NOT NULL,
    "Notas" text NOT NULL,
    "IdPlato" bigint NOT NULL,
    "IdEstado" bigint NOT NULL,
    "IdPedido" bigint NOT NULL
);
    DROP TABLE public."SubPedido";
       public         heap    postgres    false            �            1259    24655    SubPedido_IdSubPedido_seq    SEQUENCE     �   ALTER TABLE public."SubPedido" ALTER COLUMN "IdSubPedido" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."SubPedido_IdSubPedido_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
    CYCLE
);
            public          postgres    false    231            �            1259    24586    Usuarios    TABLE       CREATE TABLE public."Usuarios" (
    "IdUsuario" bigint NOT NULL,
    "Nombre" text NOT NULL,
    "Usuario" text NOT NULL,
    "Contrasena" text NOT NULL,
    "Telefono" text NOT NULL,
    "Estado" boolean NOT NULL,
    "IdRol" bigint NOT NULL,
    "IdEmpresa" bigint NOT NULL
);
    DROP TABLE public."Usuarios";
       public         heap    postgres    false            �            1259    24585    Usuarios_IdUsuario_seq    SEQUENCE     �   ALTER TABLE public."Usuarios" ALTER COLUMN "IdUsuario" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Usuarios_IdUsuario_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
    CYCLE
);
            public          postgres    false    217            >          0    24602    Empresas 
   TABLE DATA           Y   COPY public."Empresas" ("IdEmpresa", "Empresa", "Identificacion", "IdLocal") FROM stdin;
    public          postgres    false    219   F       B          0    24628    Estado 
   TABLE DATA           8   COPY public."Estado" ("IdEstado", "Estado") FROM stdin;
    public          postgres    false    223   /F       @          0    24622    Locales 
   TABLE DATA           .   COPY public."Locales" ("IdLocal") FROM stdin;
    public          postgres    false    221   LF       D          0    24636    Mesas 
   TABLE DATA           4   COPY public."Mesas" ("IdMesa", "Mesas") FROM stdin;
    public          postgres    false    225   iF       H          0    24650    Pedidos 
   TABLE DATA           i   COPY public."Pedidos" ("IdPedido", "Precio", "FechaYHora", "IdMesa", "IdEstado", "IdMeseso") FROM stdin;
    public          postgres    false    229   �F       F          0    24642    Platos 
   TABLE DATA           S   COPY public."Platos" ("IdPlato", "NombrePlato", "Precio", "IdEmpresa") FROM stdin;
    public          postgres    false    227   �F       :          0    24578    Roles 
   TABLE DATA           1   COPY public."Roles" ("IdRol", "Rol") FROM stdin;
    public          postgres    false    215   �F       J          0    24656 	   SubPedido 
   TABLE DATA           l   COPY public."SubPedido" ("IdSubPedido", "Cantidad", "Notas", "IdPlato", "IdEstado", "IdPedido") FROM stdin;
    public          postgres    false    231   �F       <          0    24586    Usuarios 
   TABLE DATA           �   COPY public."Usuarios" ("IdUsuario", "Nombre", "Usuario", "Contrasena", "Telefono", "Estado", "IdRol", "IdEmpresa") FROM stdin;
    public          postgres    false    217   �F       Q           0    0    Empresas_IdEmpresa_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public."Empresas_IdEmpresa_seq"', 1, false);
          public          postgres    false    218            R           0    0    EstadoPedido_IdEstadoPedido_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public."EstadoPedido_IdEstadoPedido_seq"', 1, false);
          public          postgres    false    222            S           0    0    Locales_IdLocal_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public."Locales_IdLocal_seq"', 1, false);
          public          postgres    false    220            T           0    0    Mesas_IdMesa_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public."Mesas_IdMesa_seq"', 1, false);
          public          postgres    false    224            U           0    0    Pedidos_IdPedido_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public."Pedidos_IdPedido_seq"', 1, false);
          public          postgres    false    228            V           0    0    Platos_IdPlato_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public."Platos_IdPlato_seq"', 1, false);
          public          postgres    false    226            W           0    0    Roles_IdRol_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public."Roles_IdRol_seq"', 1, false);
          public          postgres    false    214            X           0    0    SubPedido_IdSubPedido_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public."SubPedido_IdSubPedido_seq"', 1, false);
          public          postgres    false    230            Y           0    0    Usuarios_IdUsuario_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public."Usuarios_IdUsuario_seq"', 1, false);
          public          postgres    false    216            �           2606    24608    Empresas Empresas_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public."Empresas"
    ADD CONSTRAINT "Empresas_pkey" PRIMARY KEY ("IdEmpresa");
 D   ALTER TABLE ONLY public."Empresas" DROP CONSTRAINT "Empresas_pkey";
       public            postgres    false    219            �           2606    24634    Estado EstadoPedido_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public."Estado"
    ADD CONSTRAINT "EstadoPedido_pkey" PRIMARY KEY ("IdEstado");
 F   ALTER TABLE ONLY public."Estado" DROP CONSTRAINT "EstadoPedido_pkey";
       public            postgres    false    223            �           2606    24626    Locales Locales_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public."Locales"
    ADD CONSTRAINT "Locales_pkey" PRIMARY KEY ("IdLocal");
 B   ALTER TABLE ONLY public."Locales" DROP CONSTRAINT "Locales_pkey";
       public            postgres    false    221            �           2606    24640    Mesas Mesas_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public."Mesas"
    ADD CONSTRAINT "Mesas_pkey" PRIMARY KEY ("IdMesa");
 >   ALTER TABLE ONLY public."Mesas" DROP CONSTRAINT "Mesas_pkey";
       public            postgres    false    225            �           2606    24654    Pedidos Pedidos_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public."Pedidos"
    ADD CONSTRAINT "Pedidos_pkey" PRIMARY KEY ("IdPedido");
 B   ALTER TABLE ONLY public."Pedidos" DROP CONSTRAINT "Pedidos_pkey";
       public            postgres    false    229            �           2606    24648    Platos Platos_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public."Platos"
    ADD CONSTRAINT "Platos_pkey" PRIMARY KEY ("IdPlato");
 @   ALTER TABLE ONLY public."Platos" DROP CONSTRAINT "Platos_pkey";
       public            postgres    false    227            �           2606    24582    Roles Roles_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public."Roles"
    ADD CONSTRAINT "Roles_pkey" PRIMARY KEY ("IdRol");
 >   ALTER TABLE ONLY public."Roles" DROP CONSTRAINT "Roles_pkey";
       public            postgres    false    215            �           2606    24662    SubPedido SubPedido_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public."SubPedido"
    ADD CONSTRAINT "SubPedido_pkey" PRIMARY KEY ("IdSubPedido");
 F   ALTER TABLE ONLY public."SubPedido" DROP CONSTRAINT "SubPedido_pkey";
       public            postgres    false    231            �           2606    24620    Usuarios Usuario 
   CONSTRAINT     h   ALTER TABLE ONLY public."Usuarios"
    ADD CONSTRAINT "Usuario" UNIQUE ("Usuario") INCLUDE ("Usuario");
 >   ALTER TABLE ONLY public."Usuarios" DROP CONSTRAINT "Usuario";
       public            postgres    false    217            �           2606    24592    Usuarios Usuarios_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public."Usuarios"
    ADD CONSTRAINT "Usuarios_pkey" PRIMARY KEY ("IdUsuario");
 D   ALTER TABLE ONLY public."Usuarios" DROP CONSTRAINT "Usuarios_pkey";
       public            postgres    false    217            �           2606    24614    Usuarios IdEmpresa    FK CONSTRAINT     �   ALTER TABLE ONLY public."Usuarios"
    ADD CONSTRAINT "IdEmpresa" FOREIGN KEY ("IdEmpresa") REFERENCES public."Empresas"("IdEmpresa") NOT VALID;
 @   ALTER TABLE ONLY public."Usuarios" DROP CONSTRAINT "IdEmpresa";
       public          postgres    false    217    219    3220            �           2606    24668    Platos IdEmpresa    FK CONSTRAINT     �   ALTER TABLE ONLY public."Platos"
    ADD CONSTRAINT "IdEmpresa" FOREIGN KEY ("IdEmpresa") REFERENCES public."Empresas"("IdEmpresa") NOT VALID;
 >   ALTER TABLE ONLY public."Platos" DROP CONSTRAINT "IdEmpresa";
       public          postgres    false    219    3220    227            �           2606    24688    SubPedido IdEstado    FK CONSTRAINT     �   ALTER TABLE ONLY public."SubPedido"
    ADD CONSTRAINT "IdEstado" FOREIGN KEY ("IdEstado") REFERENCES public."Estado"("IdEstado") NOT VALID;
 @   ALTER TABLE ONLY public."SubPedido" DROP CONSTRAINT "IdEstado";
       public          postgres    false    231    223    3224            �           2606    24728    Pedidos IdEstado    FK CONSTRAINT     �   ALTER TABLE ONLY public."Pedidos"
    ADD CONSTRAINT "IdEstado" FOREIGN KEY ("IdEstado") REFERENCES public."Estado"("IdEstado") NOT VALID;
 >   ALTER TABLE ONLY public."Pedidos" DROP CONSTRAINT "IdEstado";
       public          postgres    false    3224    229    223            �           2606    24663    Empresas IdLocal    FK CONSTRAINT     �   ALTER TABLE ONLY public."Empresas"
    ADD CONSTRAINT "IdLocal" FOREIGN KEY ("IdLocal") REFERENCES public."Empresas"("IdEmpresa") NOT VALID;
 >   ALTER TABLE ONLY public."Empresas" DROP CONSTRAINT "IdLocal";
       public          postgres    false    219    3220    219            �           2606    24723    Pedidos IdMesa    FK CONSTRAINT     �   ALTER TABLE ONLY public."Pedidos"
    ADD CONSTRAINT "IdMesa" FOREIGN KEY ("IdMesa") REFERENCES public."Mesas"("IdMesa") NOT VALID;
 <   ALTER TABLE ONLY public."Pedidos" DROP CONSTRAINT "IdMesa";
       public          postgres    false    225    3226    229            �           2606    24733    Pedidos IdMesero    FK CONSTRAINT     �   ALTER TABLE ONLY public."Pedidos"
    ADD CONSTRAINT "IdMesero" FOREIGN KEY ("IdMeseso") REFERENCES public."Usuarios"("IdUsuario") NOT VALID;
 >   ALTER TABLE ONLY public."Pedidos" DROP CONSTRAINT "IdMesero";
       public          postgres    false    229    217    3218            �           2606    24683    SubPedido IdPedido    FK CONSTRAINT     �   ALTER TABLE ONLY public."SubPedido"
    ADD CONSTRAINT "IdPedido" FOREIGN KEY ("IdPedido") REFERENCES public."Pedidos"("IdPedido") NOT VALID;
 @   ALTER TABLE ONLY public."SubPedido" DROP CONSTRAINT "IdPedido";
       public          postgres    false    3230    231    229            �           2606    24673    SubPedido IdPlato    FK CONSTRAINT     �   ALTER TABLE ONLY public."SubPedido"
    ADD CONSTRAINT "IdPlato" FOREIGN KEY ("IdPlato") REFERENCES public."Platos"("IdPlato") NOT VALID;
 ?   ALTER TABLE ONLY public."SubPedido" DROP CONSTRAINT "IdPlato";
       public          postgres    false    227    3228    231            �           2606    24609    Usuarios IdRol    FK CONSTRAINT     �   ALTER TABLE ONLY public."Usuarios"
    ADD CONSTRAINT "IdRol" FOREIGN KEY ("IdRol") REFERENCES public."Roles"("IdRol") NOT VALID;
 <   ALTER TABLE ONLY public."Usuarios" DROP CONSTRAINT "IdRol";
       public          postgres    false    215    3214    217            >      x������ � �      B      x������ � �      @      x������ � �      D      x������ � �      H      x������ � �      F      x������ � �      :      x������ � �      J      x������ � �      <      x������ � �     