// Render Prop
import React from "react";

import { Formik, Form, Field, ErrorMessage } from "formik";

import { genre, countries } from "./options";

type FormErrors = {
  name?: string;
};

type SearchFormProps = {
  handleSubmit: Function;
};

export type Option = {
  id: number | string;
  name: string;
};

const DEFAULTS = {
  GENRE: {
    POP: 462882,
    ROCK: 462884,
  },
  COUNTRY: "US",
  CAREER_STAGE: "mid-level",
};

const SearchForm = ({ handleSubmit }: SearchFormProps) => (
  <div className="searchForm">
    <Formik
      initialValues={{
        name: "",
        target_genre: DEFAULTS.GENRE.ROCK,
        my_genre: DEFAULTS.GENRE.POP,
        career_stage: DEFAULTS.CAREER_STAGE,
        target_country: DEFAULTS.COUNTRY,
      }}
      validate={(values) => {
        const errors: FormErrors = {};
        if (!values.name) {
          errors.name = "Required";
        }
        return errors;
      }}
      onSubmit={(values, { setSubmitting }) => {
        handleSubmit(values, () => {
          setSubmitting(false);
        });
      }}
    >
      {({ isSubmitting }) => (
        <Form>
          <div className="field">
            <label htmlFor="name">
              <span>Your Name</span>
              <Field type="text" name="name" placeholder="Ex: Fave" id="name" />
            </label>
            <ErrorMessage name="name" component="div" className="error" />
          </div>

          <div className="field">
            <label htmlFor="target_genre">
              <span>Genre you would like to collaborate in</span>
              <Field
                as="select"
                name="target_genre"
                id="target_genre"
                defaultValue={DEFAULTS.GENRE.ROCK}
              >
                {genre.map((g: Option) => (
                  <option value={g.id} key={g.id}>
                    {g.name}
                  </option>
                ))}
              </Field>
            </label>
            <ErrorMessage
              name="target_genre"
              component="div"
              className="error"
            />
          </div>

          <div className="field">
            <label htmlFor="my_genre">
              <span>Genre that best describes you</span>
              <Field
                as="select"
                name="my_genre"
                id="my_genre"
                defaultValue={DEFAULTS.GENRE.POP}
              >
                {genre.map((g: Option, idx: number) => (
                  <option value={g.id} key={g.id}>
                    {g.name}
                  </option>
                ))}
              </Field>
            </label>
            <ErrorMessage name="my_genre" component="div" className="error" />
          </div>

          <div className="field">
            <label htmlFor="career_stage">
              <span>
                Career Stage of the artists you would like to collaborate with
              </span>
              <Field as="select" name="career_stage" defaultValue="mid-level">
                <option value="undiscovered">Undiscovered</option>
                <option value="developing">Developing</option>
                <option value="mid-level">Mid-level</option>
                <option value="mainstream">Mainstream</option>
                <option value="superstar">Superstar</option>
                <option value="legendary">Legendary</option>
              </Field>
            </label>
            <ErrorMessage
              name="career_stage"
              component="div"
              className="error"
            />
          </div>

          <div className="field">
            <label htmlFor="target_country">
              <span>Target market you would like to expand to</span>
              <Field
                as="select"
                name="target_country"
                id="target_country"
                defaultValue={DEFAULTS.COUNTRY}
              >
                {countries.map((c: Option) => (
                  <option value={c.id} key={c.id}>
                    {c.name}
                  </option>
                ))}
              </Field>
            </label>
            <ErrorMessage
              name="target_country"
              component="div"
              className="error"
            />
          </div>

          <button type="submit" disabled={isSubmitting}>
            Search
          </button>
        </Form>
      )}
    </Formik>
  </div>
);

export default SearchForm;
