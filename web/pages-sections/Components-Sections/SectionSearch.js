import React, { useState, useEffect } from "react";
// plugin that creates slider
import Slider from "nouislider";
// @material-ui/core components
import { makeStyles } from "@material-ui/core/styles";
import InputAdornment from "@material-ui/core/InputAdornment";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import Checkbox from "@material-ui/core/Checkbox";
import Radio from "@material-ui/core/Radio";
import Switch from "@material-ui/core/Switch";
// @material-ui/icons
import Favorite from "@material-ui/icons/Favorite";
import People from "@material-ui/icons/People";
import Check from "@material-ui/icons/Check";
import FiberManualRecord from "@material-ui/icons/FiberManualRecord";
// core components
import GridContainer from "/components/Grid/GridContainer.js";
import GridItem from "/components/Grid/GridItem.js";
import Button from "/components/CustomButtons/Button.js";
import CustomInput from "/components/CustomInput/CustomInput.js";
import CustomLinearProgress from "/components/CustomLinearProgress/CustomLinearProgress.js";
import Paginations from "/components/Pagination/Pagination.js";
import Badge from "/components/Badge/Badge.js";

import styles from "/styles/jss/nextjs-material-kit/pages/componentsSections/basicsStyle.js";

const useStyles = makeStyles(styles);

export default function SectionBasics() {
  const classes = useStyles();
  const [summonerName, setSummonerName] = useState("");
  const [tagline, setTagline] = useState("");
  const [apiResult, setApiResult] = useState(null); // API 결과를 저장할 상태
  const [error, setError] = useState(null); // 오류 메시지를 저장할 상태

  useEffect(() => {
    if (typeof window !== "undefined") {
      const sliderRegular = document.getElementById("sliderRegular");
      const sliderDouble = document.getElementById("sliderDouble");

      if (sliderRegular && !sliderRegular.classList.contains("noUi-target")) {
        Slider.create(sliderRegular, {
          start: [40],
          connect: [true, false],
          step: 1,
          range: { min: 0, max: 100 },
        });
      }

      if (sliderDouble && !sliderDouble.classList.contains("noUi-target")) {
        Slider.create(sliderDouble, {
          start: [20, 60],
          connect: [false, true, false],
          step: 1,
          range: { min: 0, max: 100 },
        });
      }
    }
  }, []);

  const handleInputChange = (e) => {
    const { id, value } = e.target;
    if (id === "summonerName") {
      setSummonerName(value);
    } else if (id === "tagline") {
      setTagline(value);
    }
  };

  const handleSubmit = async () => {
    // API 엔드포인트 URL
    const url = "http://slayerzeroa.iptime.org:8000/playtime";

    // API로 보낼 데이터
    const data = {
      gameName: summonerName,
      tagLine: tagline,
    };

    try {
      // API 요청 보내기
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        const result = await response.json();
        setApiResult(result); // 결과를 상태에 저장
        setError(null); // 이전 오류를 초기화
      } else {
        setApiResult(null);
        setError(`Error: ${response.status} ${response.statusText}`);
      }
    } catch (error) {
      setApiResult(null);
      setError(`Network Error: ${error.message}`);
    }
  };

  return (
    <div className={classes.sections}>
      <div className={classes.container}>
        <div id="inputs">
          <div className={classes.title}>
            <h3>[소환사명#태그라인] 입력</h3>
          </div>
          <GridContainer>
            <GridItem xs={12} sm={12} md={6}>
              <CustomInput
                labelText="소환사명"
                id="summonerName"
                formControlProps={{
                  fullWidth: true,
                }}
                inputProps={{
                  value: summonerName,
                  onChange: handleInputChange,
                }}
              />
            </GridItem>
            <GridItem xs={12} sm={12} md={6}>
              <CustomInput
                labelText="태그라인"
                id="tagline"
                formControlProps={{
                  fullWidth: true,
                }}
                inputProps={{
                  value: tagline,
                  onChange: handleInputChange,
                }}
              />
            </GridItem>
          </GridContainer>
          <Button color="primary" onClick={handleSubmit}>
            제출
          </Button>

          {/* API 결과 또는 오류 메시지를 표시 */}
          {apiResult && (
            <div style={{ marginTop: "20px", color: "green" }}>
              <h4>
                롤에 {apiResult.playtime}분을 낭비하셨습니다. <br></br> 그 시간에
                알바했으면 약 {(apiResult.playtime / 60) * 9890}원을 벌었습니다.
              </h4>
            </div>
          )}
          {error && (
            <div style={{ marginTop: "20px", color: "red" }}>
              <h4>오류:</h4>
              <p>{error}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
