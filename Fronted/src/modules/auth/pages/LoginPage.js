import React from 'react';
import {Button, Grid, TextField} from '@mui/material';
import {AuthLayout} from '../layout/AuthLayout';
import {Formik, Form, ErrorMessage} from 'formik'; // Importa Formik y Field
import * as Yup from 'yup';

export const LoginPage = () => {
  // Define el esquema de validación con Yup
  const validationSchema = Yup.object().shape({
    email: Yup.string()
      .email('Correo electrónico inválido')
      .required('Campo requerido'),
    password: Yup.string().required('Campo requerido'),
  });

  const handleSubmit = (values, {setSubmitting}) => {
    // Aquí puedes manejar la lógica de envío del formulario
    console.log(values);
    setSubmitting(false);
  };

  return (
    <AuthLayout title='Login'>
      <Formik
        initialValues={{email: '', password: ''}}
        onSubmit={handleSubmit}
        validationSchema={validationSchema}
      >
        {({isSubmitting}) => (
          <Form>
            <Grid container>
              <Grid item xs={12} sx={{mt: 2}}>
                <TextField
                  name='email'
                  label='Correo'
                  type='email'
                  placeholder='correo@google.com'
                  fullWidth
                />
                <ErrorMessage name='email' component='div' className='error' />
              </Grid>

              <Grid item xs={12} sx={{mt: 2}}>
                <TextField
                  name='password'
                  label='Contraseña'
                  type='password'
                  placeholder='Contraseña'
                  fullWidth
                />
                <ErrorMessage name='password' component='div' className='error' />
              </Grid>

              <Grid container spacing={2} sx={{mb: 2, mt: 1}}>
                <Button
                  variant='contained'
                  fullWidth
                  type='submit'
                  disabled={isSubmitting}
                >
                  {isSubmitting ? 'Enviando...' : 'Login'}
                </Button>
              </Grid>
            </Grid>
          </Form>
        )}
      </Formik>
    </AuthLayout>
  );
};
