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

--
-- Name: service; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA service;


ALTER SCHEMA service OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: users; Type: TABLE; Schema: service; Owner: postgres
--

CREATE TABLE service.users (
    id integer NOT NULL,
    full_name character varying NOT NULL,
    login character varying NOT NULL,
    password character varying NOT NULL
);


ALTER TABLE service.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: service; Owner: postgres
--

CREATE SEQUENCE service.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE service.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: service; Owner: postgres
--

ALTER SEQUENCE service.users_id_seq OWNED BY service.users.id;


--
-- Name: users id; Type: DEFAULT; Schema: service; Owner: postgres
--

ALTER TABLE ONLY service.users ALTER COLUMN id SET DEFAULT nextval('service.users_id_seq'::regclass);


--
-- Data for Name: users; Type: TABLE DATA; Schema: service; Owner: postgres
--

COPY service.users (id, full_name, login, password) FROM stdin;
2	Hetfield	papahet63	qwerty1
3	Ulrich	napster_hater63	qwerty2
4	Hammett	jovaniy_hleb62	qwerty3
5	Burton	godlike_bassist62	qwerty4
6	Newsted	menya_ne_slishno63	qwerty5
7	Trujillo	crab_guy	qwerty6
8	Mustaine	redBeauty	qwerty7
10	Darell Abbott	god_himself	qwerty9
11	Vincent Abbott	gods_brother	qwerty10
12	Brown	rocker64	qwerty11
9	Anselmo	growl_machine	qwerty8
14	Jordison	drum_daddy75	qwerty12
\.


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: service; Owner: postgres
--

SELECT pg_catalog.setval('service.users_id_seq', 17, true);


--
-- PostgreSQL database dump complete
--

