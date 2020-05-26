import React, { useState, useEffect } from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import WelcomePage from './components/WelcomePage'
import './style.scss'
import DisplayArtwork from './DisplayArtwork'
import DisplayArtist from './components/DisplayArtist'
import DisplayPeriod from './components/DisplayPeriod'
import DisplaySingleArt from './components/DisplaySingleArt'
import Navbar from './components/NavBar'
import Register from './components/Register'
import Login from './components/Login'
// import Hero from './components/Hero'

const App = () => {
  return <BrowserRouter>
    <Navbar />
    <Switch>
      <Route exact path = {'/'} component={WelcomePage}/>
      <Route exact path={'/artwork/artist'} component={DisplayArtist} />
      <Route exact path={'/artwork/period'} component={DisplayPeriod} />
      <Route exact path={'/artwork/:id'} component={DisplaySingleArt} />
      <Route exact path={'/artwork'} component={DisplayArtwork} />
      <Route path="/register" component={Register}/>
      <Route path="/login" component={Login}/>
    </Switch>
  </BrowserRouter>
}


ReactDOM.render(
  <App />,
  document.getElementById('root')
)

