import React, { useState, useEffect } from 'react'
import 'bulma'
import Hero from './Hero'


const DisplayArtist = () => {
  const [data, setData] = useState([])

  useEffect(() => {
    fetch('/api/artwork/artist')
      .then(resp => resp.json())
      .then(resp => setData(resp))
  })

  return <>
  <Hero />
  <section className="section">
    <div className="container">
      <div className="columns is-multiline">
        {data.map((artist, key) => 
          <div className="column is-one-third" key={key}>
            <div className="card">
              <div className="card-image">
                <figure className="card-image is-3by3">
                  <img src={artist.image} className="art-image"></img>
                </figure>
              </div>
              <div className="card-content">
                <h2 className="subtitle recipe">{artist.name}</h2>
              </div>
            </div>
          </div>)}
      </div>
    </div>
  </section>
</>
}

export default DisplayArtist