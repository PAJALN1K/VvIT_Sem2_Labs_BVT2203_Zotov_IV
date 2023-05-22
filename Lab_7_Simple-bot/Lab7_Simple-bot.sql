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
-- Name: subject; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.subject (
    name character varying NOT NULL
);


ALTER TABLE public.subject OWNER TO postgres;

--
-- Name: teacher; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.teacher (
    id integer NOT NULL,
    full_name character varying NOT NULL,
    subject_name character varying
);


ALTER TABLE public.teacher OWNER TO postgres;

--
-- Name: teacher_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.teacher_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.teacher_id_seq OWNER TO postgres;

--
-- Name: teacher_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.teacher_id_seq OWNED BY public.teacher.id;


--
-- Name: timetable; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.timetable (
    id integer NOT NULL,
    is_week_even integer NOT NULL,
    day character varying NOT NULL,
    room character varying NOT NULL,
    start_time character varying NOT NULL,
    subject_name character varying
);


ALTER TABLE public.timetable OWNER TO postgres;

--
-- Name: timetable_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.timetable_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.timetable_id_seq OWNER TO postgres;

--
-- Name: timetable_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.timetable_id_seq OWNED BY public.timetable.id;


--
-- Name: teacher id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teacher ALTER COLUMN id SET DEFAULT nextval('public.teacher_id_seq'::regclass);


--
-- Name: timetable id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.timetable ALTER COLUMN id SET DEFAULT nextval('public.timetable_id_seq'::regclass);


--
-- Data for Name: subject; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.subject (name) FROM stdin;
Алгебра и геометрия
Базы данных
Введение в информационные технологии
Высшая математика
Схоластика
Физкультура
DevOps
Безопасность жизнедеятельности
\.


--
-- Data for Name: teacher; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.teacher (id, full_name, subject_name) FROM stdin;
1	А. В. Курилин	Алгебра и геометрия
2	Ю. В. Полищук	Базы данных
3	В. В. Ерофеева	Безопасность жизнедеятельности
4	Ю. М. Фурлетов	Введение в информационные технологии
5	Л. К. Шаймарданова	Высшая математика
6	М. И. Иванова	Схоластика
7	С. А. Королева	Физкультура
8	М. Г. Городничев	DevOps
\.


--
-- Data for Name: timetable; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.timetable (id, is_week_even, day, room, start_time, subject_name) FROM stdin;
7	0	Вторник	Н521	11:20	Алгебра и геометрия
12	0	Четверг	Н327	09:30	Алгебра и геометрия
9	0	Вторник	Н324	15:25	Базы данных
6	0	Вторник	Н525	09:30	Высшая математика
13	0	Четверг	Н304	11:20	Схоластика
23	1	Среда	Н301	13:10	Алгебра и геометрия
24	1	Среда	Н301	15:25	Алгебра и геометрия
25	1	Четверг	Н324	09:30	Алгебра и геометрия
16	1	Понедельник	Н324	09:30	Базы данных
18	1	Понедельник	Н501	13:10	Высшая математика
19	1	Понедельник	Н501	15:25	Высшая математика
26	1	Четверг	Н525	11:20	Высшая математика
22	1	Среда	Н221	11:20	Схоластика
8	0	Вторник	Н-C/Зал	13:10	Физкультура
14	0	Четверг	Н-C/Зал	13:10	Физкультура
17	1	Понедельник	Н-C/Зал	11:20	Физкультура
1	0	Понедельник	Н001	09:30	Безопасность жизнедеятельности
2	0	Понедельник	Н001	11:20	Безопасность жизнедеятельности
3	0	Понедельник	Н001	13:10	Безопасность жизнедеятельности
4	0	Понедельник	Н001	15:25	Безопасность жизнедеятельности
5	0	Понедельник	Н001	17:15	Безопасность жизнедеятельности
15	0	Пятница	Н001	17:15	Безопасность жизнедеятельности
27	1	Пятница	Н001	17:15	Безопасность жизнедеятельности
10	0	Среда	А321	11:20	Введение в информационные технологии
11	0	Среда	А321	13:10	Введение в информационные технологии
20	1	Вторник	А321	11:20	Введение в информационные технологии
21	1	Вторник	А321	13:10	Введение в информационные технологии
\.


--
-- Name: teacher_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.teacher_id_seq', 10, true);


--
-- Name: timetable_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.timetable_id_seq', 27, true);


--
-- Name: subject subject_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subject
    ADD CONSTRAINT subject_pkey PRIMARY KEY (name);


--
-- Name: teacher teacher_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teacher
    ADD CONSTRAINT teacher_pkey PRIMARY KEY (id);


--
-- Name: timetable timetable_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.timetable
    ADD CONSTRAINT timetable_pkey PRIMARY KEY (id);


--
-- Name: teacher teacher_subject_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teacher
    ADD CONSTRAINT teacher_subject_name_fkey FOREIGN KEY (subject_name) REFERENCES public.subject(name);


--
-- Name: timetable timetable_subject_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.timetable
    ADD CONSTRAINT timetable_subject_name_fkey FOREIGN KEY (subject_name) REFERENCES public.subject(name);


--
-- PostgreSQL database dump complete
--

