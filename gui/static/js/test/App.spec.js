import { mount } from '@vue/test-utils';
import sinon from 'sinon';

import App from '../components/App.vue';
import NodeSetting from '../components/NodeSetting.vue';
import InfoList from '../components/InfoList.vue';

describe('App.vue', () => {
  let server = null;

  beforeEach(() => {
    server = sinon.fakeServer.create();
  });

  afterEach(() => {
    server.restore();
  });

  it('retrieves info', (done) => {
    const responseData = {
      reputation: 1000,
      spaceAvailable: true,
      userAgent: '8.7.1',
    };
    const response = [
      200,
      {
        'Content-type': 'application/json',
      },
      JSON.stringify(responseData),
    ];

    server.respondWith('GET', '/api/contacts/1234', response);

    const wrapper = mount(App);
    wrapper.setData({
      contactsUrl: '/api/contacts/',
    });

    wrapper.find(NodeSetting).vm.nodeId = '1234';
    wrapper.find('button').trigger('click');

    server.respond();

    setTimeout(() => {
      expect(wrapper.find(NodeSetting).vm.errorMessage).toBe('');
      expect(wrapper.find(InfoList).vm.info).toEqual(responseData);
      done();
    }, 1);
  });

  it('handles an API error', (done) => {
    const errorMessage = 'Error retrieving information: Contact not found';
    const response = [
      404,
      {
        'Content-type': 'application/json',
      },
      errorMessage,
    ];

    server.respondWith('GET', '/api/contacts/1234', response);

    const wrapper = mount(App);
    wrapper.setData({
      contactsUrl: '/api/contacts/',
    });

    wrapper.find(NodeSetting).vm.nodeId = '1234';
    wrapper.find('button').trigger('click');

    server.respond();

    setTimeout(() => {
      expect(wrapper.find(NodeSetting).vm.errorMessage).toBe(`1234: ${errorMessage}`);
      expect(wrapper.find(InfoList).vm.info).toBe(null);
      done();
    }, 1);
  });
});

