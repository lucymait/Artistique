import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import Hero from './components/Hero'
import 'bulma'

const DisplayArtwork = () => {
  const [data, setData] = useState([])

  useEffect(() => {
    fetch('/api/artwork')
      .then(resp => resp.json())
      .then(resp => setData(resp))
  }, [])

  return <>
    <Hero />
    <section className="section">
      <div className="container">
        <div className="columns is-multiline">
          {data.map((art) => {
            return <div className="column is-one-third" key={art.id}>
              <Link to={{ pathname: `artwork/${art.id}` }}>
                <div className="card">
                  <div className="card-content">
                    <h2 className="subtitle">{art.name}</h2>
                  </div>
                  <div className="card-image">
                    <figure className="card-image is-3by3">
                      <img src={art.image} className="art-image"></img>
                    </figure>
                  </div>
                </div>
              </Link>
            </div>
          })}
        </div>
      </div>
    </section>
  </>
}

export default DisplayArtwork