import React from 'react';
import {Button, Grid, TextField} from '@mui/material';
import {AuthLayout} from '../layout/AuthLayout';
import {Formik, Form, ErrorMessage} from 'formik';
import * as Yup from 'yup';
import { useNavigate } from 'react-router-dom';



function LoginPage() {

  const navigate = useNavigate();

  const validationSchema = Yup.object().shape({
    email: Yup.string()
      .email('Correo electrónico inválido')
      .required('Campo requerido'),
    password: Yup.string().required('Campo requerido'),
  });

  const handleSubmit = (values, {setSubmitting}) => {
    navigate("/");
    console.log(values);
    setSubmitting(false);
  };

  return (
    <AuthLayout title='Login'>
      <Formik
        initialValues={{email: '', password: ''}}
        onSubmit={handleSubmit}
      >
        {({isSubmitting, errors, touched}) => (
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
                {errors.email && touched.email && (
                  <div className='error' style={{color: 'red'}}>
                    {errors.email}
                  </div>
                )}
              </Grid>

              <Grid item xs={12} sx={{mt: 2}}>
                <TextField
                  name='password'
                  label='Contraseña'
                  type='password'
                  placeholder='Contraseña'
                  fullWidth
                />
                {errors.password && touched.password && (
                  <div className='error' style={{color: 'red'}}>
                    {errors.password}
                  </div>
                )}
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

export default LoginPage