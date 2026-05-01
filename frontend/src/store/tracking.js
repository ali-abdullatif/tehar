import axios from 'axios';
import { v4 as uuidv4 } from 'uuid';

const API_URL = 'http://tihar.site:8000';

const getSessionId = () => {
  let sessionId = localStorage.getItem('shop_session_id');
  if (!sessionId) {
    sessionId = uuidv4();
    localStorage.setItem('shop_session_id', sessionId);
  }
  return sessionId;
};

export const trackEvent = async (type, productId = null, quantity = 1, metadata = {}) => {
  try {
    await axios.post(`${API_URL}/analytics/track`, {
      event_type: type,
      product_id: productId,
      quantity,
      session_id: getSessionId(),
      metadata_json: JSON.stringify(metadata)
    });
  } catch (e) {
    console.error('Tracking error:', e);
  }
};
