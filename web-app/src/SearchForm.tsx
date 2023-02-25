// Render Prop
import React from 'react';

import { Formik, Form, Field, ErrorMessage } from 'formik';

type FormErrors = {
  searchText?: string
};

type SearchFormProps = {
  handleSubmit: Function
};

const SearchForm = ({ handleSubmit }: SearchFormProps) => (
  <div className='searchForm'>
    <Formik
      initialValues={{ searchText: '' }}
      validate={values => {
        const errors: FormErrors = {};
        if (!values.searchText) {
          errors.searchText = 'Required';
        }
        return errors;
      }}
      onSubmit={(values, { setSubmitting }) => {
        handleSubmit()
      }}
    >
      {({ isSubmitting }) => (
        <Form>
          <Field type="text" name="searchText" placeholder="Your track's Soundcloud URL"/>
          <ErrorMessage name="searchText" component="div" className='error'/>
          <button type="submit" disabled={isSubmitting}>
            Search
          </button>
        </Form>
      )}
    </Formik>
  </div>
);

export default SearchForm;