PGDMP         -                {            poo    12.16    12.16 <    e           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            f           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            g           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            h           1262    16393    poo    DATABASE     �   CREATE DATABASE poo WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Spanish_Spain.1252' LC_CTYPE = 'Spanish_Spain.1252';
    DROP DATABASE poo;
                postgres    false            �            1259    16394    Empresas    TABLE     �   CREATE TABLE public."Empresas" (
    "IdEmpresa" bigint NOT NULL,
    "Empresa" text NOT NULL,
    "Identificacion" bigint NOT NULL,
    "IdLocal" bigint NOT NULL
);
    DROP TABLE public."Empresas";
       public         heap    postgres    false            �            1259    16400    Empresas_IdEmpresa_seq    SEQUENCE     �   ALTER TABLE public."Empresas" ALTER COLUMN "IdEmpresa" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Empresas_IdEmpresa_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
    CYCLE
);
            public          postgres    false    202            �            1259    16402    Estado    TABLE     ]   CREATE TABLE public."Estado" (
    "IdEstado" bigint NOT NULL,
    "Estado" text NOT NULL
);
    DROP TABLE public."Estado";
       public         heap    postgres    false            �            1259    16408    EstadoPedido_IdEstadoPedido_seq    SEQUENCE     �   ALTER TABLE public."Estado" ALTER COLUMN "IdEstado" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."EstadoPedido_IdEstadoPedido_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
    CYCLE
);
            public          postgres    false    204            �            1259    16410    Locales    TABLE     U   CREATE TABLE public."Locales" (
    "IdLocal" bigint NOT NULL,
    "Local" bigint
);
    DROP TABLE public."Locales";
       public         heap    postgres    false            �            1259    16413    Locales_IdLocal_seq    SEQUENCE     �   ALTER TABLE public."Locales" ALTER COLUMN "IdLocal" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Locales_IdLocal_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
    CYCLE
);
            public          postgres    false    206            �            1259    16415    Mesas    TABLE     R   CREATE TABLE public."Mesas" (
    "IdMesa" bigint NOT NULL,
    "Mesas" bigint
);
    DROP TABLE public."Mesas";
       public         heap    postgres    false            �            1259    16418    Mesas_IdMesa_seq    SEQUENCE     �   ALTER TABLE public."Mesas" ALTER COLUMN "IdMesa" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Mesas_IdMesa_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
    CYCLE
);
            public          postgres    false    208            �            1259    16420    Pedidos    TABLE     �   CREATE TABLE public."Pedidos" (
    "IdPedido" bigint NOT NULL,
    "Precio" bigint,
    "FechaYHora" timestamp with time zone,
    "IdMesa" bigint NOT NULL,
    "IdEstado" bigint NOT NULL,
    "IdMesero" bigint NOT NULL
);
    DROP TABLE public."Pedidos";
       public         heap    postgres    false            �            1259    16423    Pedidos_IdPedido_seq    SEQUENCE     �   ALTER TABLE public."Pedidos" ALTER COLUMN "IdPedido" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Pedidos_IdPedido_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
    CYCLE
);
            public          postgres    false    210            �            1259    16425    Platos    TABLE     �   CREATE TABLE public."Platos" (
    "IdPlato" bigint NOT NULL,
    "NombrePlato" text NOT NULL,
    "Precio" bigint NOT NULL,
    "IdEmpresa" bigint
);
    DROP TABLE public."Platos";
       public         heap    postgres    false            �            1259    16431    Platos_IdPlato_seq    SEQUENCE     �   ALTER TABLE public."Platos" ALTER COLUMN "IdPlato" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Platos_IdPlato_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
    CYCLE
);
            public          postgres    false    212            �            1259    16433    Roles    TABLE     M   CREATE TABLE public."Roles" (
    "IdRol" bigint NOT NULL,
    "Rol" text
);
    DROP TABLE public."Roles";
       public         heap    postgres    false            �            1259    16439    Roles_IdRol_seq    SEQUENCE     �   ALTER TABLE public."Roles" ALTER COLUMN "IdRol" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Roles_IdRol_seq"
    START WITH 1
    INCREMENT BY 1
    MINVALUE 0
    NO MAXVALUE
    CACHE 1
    CYCLE
);
            public          postgres    false    214            �            1259    16441 	   SubPedido    TABLE     �   CREATE TABLE public."SubPedido" (
    "IdSubPedido" bigint NOT NULL,
    "Cantidad" bigint NOT NULL,
    "Notas" text NOT NULL,
    "IdPlato" bigint NOT NULL,
    "IdEstado" bigint NOT NULL,
    "IdPedido" bigint NOT NULL
);
    DROP TABLE public."SubPedido";
       public         heap    postgres    false            �            1259    16447    SubPedido_IdSubPedido_seq    SEQUENCE     �   ALTER TABLE public."SubPedido" ALTER COLUMN "IdSubPedido" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."SubPedido_IdSubPedido_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
    CYCLE
);
            public          postgres    false    216            �            1259    16449    Usuarios    TABLE       CREATE TABLE public."Usuarios" (
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
       public         heap    postgres    false            �            1259    16455    Usuarios_IdUsuario_seq    SEQUENCE     �   ALTER TABLE public."Usuarios" ALTER COLUMN "IdUsuario" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Usuarios_IdUsuario_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
    CYCLE
);
            public          postgres    false    218            Q          0    16394    Empresas 
   TABLE DATA           Y   COPY public."Empresas" ("IdEmpresa", "Empresa", "Identificacion", "IdLocal") FROM stdin;
    public          postgres    false    202   )F       S          0    16402    Estado 
   TABLE DATA           8   COPY public."Estado" ("IdEstado", "Estado") FROM stdin;
    public          postgres    false    204   ]F       U          0    16410    Locales 
   TABLE DATA           7   COPY public."Locales" ("IdLocal", "Local") FROM stdin;
    public          postgres    false    206   �F       W          0    16415    Mesas 
   TABLE DATA           4   COPY public."Mesas" ("IdMesa", "Mesas") FROM stdin;
    public          postgres    false    208   �F       Y          0    16420    Pedidos 
   TABLE DATA           i   COPY public."Pedidos" ("IdPedido", "Precio", "FechaYHora", "IdMesa", "IdEstado", "IdMesero") FROM stdin;
    public          postgres    false    210   �F       [          0    16425    Platos 
   TABLE DATA           S   COPY public."Platos" ("IdPlato", "NombrePlato", "Precio", "IdEmpresa") FROM stdin;
    public          postgres    false    212   G       ]          0    16433    Roles 
   TABLE DATA           1   COPY public."Roles" ("IdRol", "Rol") FROM stdin;
    public          postgres    false    214   G       _          0    16441 	   SubPedido 
   TABLE DATA           l   COPY public."SubPedido" ("IdSubPedido", "Cantidad", "Notas", "IdPlato", "IdEstado", "IdPedido") FROM stdin;
    public          postgres    false    216   lG       a          0    16449    Usuarios 
   TABLE DATA           �   COPY public."Usuarios" ("IdUsuario", "Nombre", "Usuario", "Contrasena", "Telefono", "Estado", "IdRol", "IdEmpresa") FROM stdin;
    public          postgres    false    218   �G       i           0    0    Empresas_IdEmpresa_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public."Empresas_IdEmpresa_seq"', 1, true);
          public          postgres    false    203            j           0    0    EstadoPedido_IdEstadoPedido_seq    SEQUENCE SET     O   SELECT pg_catalog.setval('public."EstadoPedido_IdEstadoPedido_seq"', 4, true);
          public          postgres    false    205            k           0    0    Locales_IdLocal_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public."Locales_IdLocal_seq"', 1, true);
          public          postgres    false    207            l           0    0    Mesas_IdMesa_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public."Mesas_IdMesa_seq"', 1, false);
          public          postgres    false    209            m           0    0    Pedidos_IdPedido_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public."Pedidos_IdPedido_seq"', 1, false);
          public          postgres    false    211            n           0    0    Platos_IdPlato_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public."Platos_IdPlato_seq"', 1, false);
          public          postgres    false    213            o           0    0    Roles_IdRol_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public."Roles_IdRol_seq"', 5, true);
          public          postgres    false    215            p           0    0    SubPedido_IdSubPedido_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public."SubPedido_IdSubPedido_seq"', 1, false);
          public          postgres    false    217            q           0    0    Usuarios_IdUsuario_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public."Usuarios_IdUsuario_seq"', 4, true);
          public          postgres    false    219            �
           2606    16458    Empresas Empresas_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public."Empresas"
    ADD CONSTRAINT "Empresas_pkey" PRIMARY KEY ("IdEmpresa");
 D   ALTER TABLE ONLY public."Empresas" DROP CONSTRAINT "Empresas_pkey";
       public            postgres    false    202            �
           2606    16460    Estado EstadoPedido_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public."Estado"
    ADD CONSTRAINT "EstadoPedido_pkey" PRIMARY KEY ("IdEstado");
 F   ALTER TABLE ONLY public."Estado" DROP CONSTRAINT "EstadoPedido_pkey";
       public            postgres    false    204            �
           2606    16462    Locales Locales_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public."Locales"
    ADD CONSTRAINT "Locales_pkey" PRIMARY KEY ("IdLocal");
 B   ALTER TABLE ONLY public."Locales" DROP CONSTRAINT "Locales_pkey";
       public            postgres    false    206            �
           2606    16464    Mesas Mesas_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public."Mesas"
    ADD CONSTRAINT "Mesas_pkey" PRIMARY KEY ("IdMesa");
 >   ALTER TABLE ONLY public."Mesas" DROP CONSTRAINT "Mesas_pkey";
       public            postgres    false    208            �
           2606    16466    Pedidos Pedidos_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public."Pedidos"
    ADD CONSTRAINT "Pedidos_pkey" PRIMARY KEY ("IdPedido");
 B   ALTER TABLE ONLY public."Pedidos" DROP CONSTRAINT "Pedidos_pkey";
       public            postgres    false    210            �
           2606    16468    Platos Platos_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public."Platos"
    ADD CONSTRAINT "Platos_pkey" PRIMARY KEY ("IdPlato");
 @   ALTER TABLE ONLY public."Platos" DROP CONSTRAINT "Platos_pkey";
       public            postgres    false    212            �
           2606    16470    Roles Roles_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public."Roles"
    ADD CONSTRAINT "Roles_pkey" PRIMARY KEY ("IdRol");
 >   ALTER TABLE ONLY public."Roles" DROP CONSTRAINT "Roles_pkey";
       public            postgres    false    214            �
           2606    16472    SubPedido SubPedido_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public."SubPedido"
    ADD CONSTRAINT "SubPedido_pkey" PRIMARY KEY ("IdSubPedido");
 F   ALTER TABLE ONLY public."SubPedido" DROP CONSTRAINT "SubPedido_pkey";
       public            postgres    false    216            �
           2606    16474    Usuarios Usuario 
   CONSTRAINT     h   ALTER TABLE ONLY public."Usuarios"
    ADD CONSTRAINT "Usuario" UNIQUE ("Usuario") INCLUDE ("Usuario");
 >   ALTER TABLE ONLY public."Usuarios" DROP CONSTRAINT "Usuario";
       public            postgres    false    218    218            �
           2606    16476    Usuarios Usuarios_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public."Usuarios"
    ADD CONSTRAINT "Usuarios_pkey" PRIMARY KEY ("IdUsuario");
 D   ALTER TABLE ONLY public."Usuarios" DROP CONSTRAINT "Usuarios_pkey";
       public            postgres    false    218            �
           2606    16477    Usuarios IdEmpresa    FK CONSTRAINT     �   ALTER TABLE ONLY public."Usuarios"
    ADD CONSTRAINT "IdEmpresa" FOREIGN KEY ("IdEmpresa") REFERENCES public."Empresas"("IdEmpresa") NOT VALID;
 @   ALTER TABLE ONLY public."Usuarios" DROP CONSTRAINT "IdEmpresa";
       public          postgres    false    218    2742    202            �
           2606    16482    Platos IdEmpresa    FK CONSTRAINT     �   ALTER TABLE ONLY public."Platos"
    ADD CONSTRAINT "IdEmpresa" FOREIGN KEY ("IdEmpresa") REFERENCES public."Empresas"("IdEmpresa") NOT VALID;
 >   ALTER TABLE ONLY public."Platos" DROP CONSTRAINT "IdEmpresa";
       public          postgres    false    202    2742    212            �
           2606    16487    SubPedido IdEstado    FK CONSTRAINT     �   ALTER TABLE ONLY public."SubPedido"
    ADD CONSTRAINT "IdEstado" FOREIGN KEY ("IdEstado") REFERENCES public."Estado"("IdEstado") NOT VALID;
 @   ALTER TABLE ONLY public."SubPedido" DROP CONSTRAINT "IdEstado";
       public          postgres    false    2744    204    216            �
           2606    16492    Pedidos IdEstado    FK CONSTRAINT     �   ALTER TABLE ONLY public."Pedidos"
    ADD CONSTRAINT "IdEstado" FOREIGN KEY ("IdEstado") REFERENCES public."Estado"("IdEstado") NOT VALID;
 >   ALTER TABLE ONLY public."Pedidos" DROP CONSTRAINT "IdEstado";
       public          postgres    false    210    2744    204            �
           2606    16497    Empresas IdLocal    FK CONSTRAINT     �   ALTER TABLE ONLY public."Empresas"
    ADD CONSTRAINT "IdLocal" FOREIGN KEY ("IdLocal") REFERENCES public."Empresas"("IdEmpresa") NOT VALID;
 >   ALTER TABLE ONLY public."Empresas" DROP CONSTRAINT "IdLocal";
       public          postgres    false    202    2742    202            �
           2606    16502    Pedidos IdMesa    FK CONSTRAINT     �   ALTER TABLE ONLY public."Pedidos"
    ADD CONSTRAINT "IdMesa" FOREIGN KEY ("IdMesa") REFERENCES public."Mesas"("IdMesa") NOT VALID;
 <   ALTER TABLE ONLY public."Pedidos" DROP CONSTRAINT "IdMesa";
       public          postgres    false    208    210    2748            �
           2606    16507    Pedidos IdMesero    FK CONSTRAINT     �   ALTER TABLE ONLY public."Pedidos"
    ADD CONSTRAINT "IdMesero" FOREIGN KEY ("IdMesero") REFERENCES public."Usuarios"("IdUsuario") NOT VALID;
 >   ALTER TABLE ONLY public."Pedidos" DROP CONSTRAINT "IdMesero";
       public          postgres    false    218    2760    210            �
           2606    16512    SubPedido IdPedido    FK CONSTRAINT     �   ALTER TABLE ONLY public."SubPedido"
    ADD CONSTRAINT "IdPedido" FOREIGN KEY ("IdPedido") REFERENCES public."Pedidos"("IdPedido") NOT VALID;
 @   ALTER TABLE ONLY public."SubPedido" DROP CONSTRAINT "IdPedido";
       public          postgres    false    210    2750    216            �
           2606    16517    SubPedido IdPlato    FK CONSTRAINT     �   ALTER TABLE ONLY public."SubPedido"
    ADD CONSTRAINT "IdPlato" FOREIGN KEY ("IdPlato") REFERENCES public."Platos"("IdPlato") NOT VALID;
 ?   ALTER TABLE ONLY public."SubPedido" DROP CONSTRAINT "IdPlato";
       public          postgres    false    212    216    2752            �
           2606    16522    Usuarios IdRol    FK CONSTRAINT     �   ALTER TABLE ONLY public."Usuarios"
    ADD CONSTRAINT "IdRol" FOREIGN KEY ("IdRol") REFERENCES public."Roles"("IdRol") NOT VALID;
 <   ALTER TABLE ONLY public."Usuarios" DROP CONSTRAINT "IdRol";
       public          postgres    false    2754    218    214            Q   $   x�3�r��44063254�01�4����� V>C      S   :   x�3�t�S((�ON-��2�(J-H,JL��2�tN�KN��M8�2�s2�@�=... �l�      U      x�3�4����� ]      W      x������ � �      Y      x������ � �      [      x������ � �      ]   =   x�3�tL����,.)JL�/R��ON��2��M-N-��2�t�O��1M�T����jc���� [+      _      x������ � �      a      x������ � �     