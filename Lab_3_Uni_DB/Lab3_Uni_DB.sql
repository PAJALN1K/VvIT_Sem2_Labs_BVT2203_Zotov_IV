--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: chair; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.chair (
    chair_id integer NOT NULL,
    chair_name character varying NOT NULL,
    chair_deanery character varying NOT NULL
);


ALTER TABLE public.chair OWNER TO postgres;

--
-- Name: chair_chair_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.chair_chair_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.chair_chair_id_seq OWNER TO postgres;

--
-- Name: chair_chair_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.chair_chair_id_seq OWNED BY public.chair.chair_id;


--
-- Name: student; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student (
    student_id integer NOT NULL,
    student_surname character varying NOT NULL,
    student_name character varying NOT NULL,
    student_passport character varying(6) NOT NULL,
    fk_student_uni_group character varying
);


ALTER TABLE public.student OWNER TO postgres;

--
-- Name: student_student_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.student_student_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.student_student_id_seq OWNER TO postgres;

--
-- Name: student_student_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.student_student_id_seq OWNED BY public.student.student_id;


--
-- Name: uni_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.uni_group (
    uni_group_id integer NOT NULL,
    uni_group_name character varying NOT NULL,
    fk_uni_group_chair character varying
);


ALTER TABLE public.uni_group OWNER TO postgres;

--
-- Name: uni_group_uni_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.uni_group_uni_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.uni_group_uni_group_id_seq OWNER TO postgres;

--
-- Name: uni_group_uni_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.uni_group_uni_group_id_seq OWNED BY public.uni_group.uni_group_id;


--
-- Name: chair chair_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.chair ALTER COLUMN chair_id SET DEFAULT nextval('public.chair_chair_id_seq'::regclass);


--
-- Name: student student_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student ALTER COLUMN student_id SET DEFAULT nextval('public.student_student_id_seq'::regclass);


--
-- Name: uni_group uni_group_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.uni_group ALTER COLUMN uni_group_id SET DEFAULT nextval('public.uni_group_uni_group_id_seq'::regclass);


--
-- Data for Name: chair; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.chair (chair_id, chair_name, chair_deanery) FROM stdin;
1	Информатика	Зотов И.В.
2	Иностранный язык	Дворянчиков Д.Д.
\.


--
-- Data for Name: student; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student (student_id, student_surname, student_name, student_passport, fk_student_uni_group) FROM stdin;
1	Шáшилов	Андрей	000001	БТС2203
2	Шаши́лов	Андрей	000002	БТС2203
3	Шашило́в	Андрей	000003	БТС2203
4	Шáшилов	Алексей	000004	БТС2203
5	Шаши́лов	Алексей	000005	БТС2203
6	Шашило́в	Алексей	000006	БМВ2202
7	Шáмилов	Андрей	000011	БМВ2202
8	Шами́лов	Андрей	000012	БМВ2202
9	Шамило́в	Андрей	000013	БМВ2202
10	Шáмилов	Алексей	000014	БМВ2202
11	Шами́лов	Алексей	000015	БИБ2020
12	Шамило́в	Алексей	000016	БИБ2020
13	И́смаилов	Андрей	000021	БИБ2020
14	Исмáилов	Андрей	000022	БИБ2020
15	Исмаи́лов	Андрей	000023	БИБ2020
16	Исмаило́в	Андрей	000024	БОБ2120
17	И́смаилов	Андрей	000025	БОБ2120
18	Исмáилов	Алексей	000026	БОБ2120
19	Исмаи́лов	Алексей	000027	БОБ2120
20	Исмаило́в	Алексей	000028	БОБ2120
\.


--
-- Data for Name: uni_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.uni_group (uni_group_id, uni_group_name, fk_uni_group_chair) FROM stdin;
1	БТС2203	Информатика
2	БИБ2020	Иностранный язык
3	БМВ2202	Информатика
4	БОБ2120	Иностранный язык
\.


--
-- Name: chair_chair_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.chair_chair_id_seq', 2, true);


--
-- Name: student_student_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.student_student_id_seq', 20, true);


--
-- Name: uni_group_uni_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.uni_group_uni_group_id_seq', 4, true);


--
-- Name: chair chair_chair_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.chair
    ADD CONSTRAINT chair_chair_name_key UNIQUE (chair_name);


--
-- Name: chair chair_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.chair
    ADD CONSTRAINT chair_pkey PRIMARY KEY (chair_id);


--
-- Name: student student_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_pkey PRIMARY KEY (student_id);


--
-- Name: student student_student_passport_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_student_passport_key UNIQUE (student_passport);


--
-- Name: uni_group uni_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.uni_group
    ADD CONSTRAINT uni_group_pkey PRIMARY KEY (uni_group_id);


--
-- Name: uni_group uni_group_uni_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.uni_group
    ADD CONSTRAINT uni_group_uni_group_name_key UNIQUE (uni_group_name);


--
-- Name: student student_fk_student_uni_group_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student
    ADD CONSTRAINT student_fk_student_uni_group_fkey FOREIGN KEY (fk_student_uni_group) REFERENCES public.uni_group(uni_group_name);


--
-- Name: uni_group uni_group_fk_uni_group_chair_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.uni_group
    ADD CONSTRAINT uni_group_fk_uni_group_chair_fkey FOREIGN KEY (fk_uni_group_chair) REFERENCES public.chair(chair_name);


--
-- PostgreSQL database dump complete
--

